import subprocess
import os
import sys
from pathlib import Path

def setup_task_scheduler():
    """Adds a daily task to Windows Task Scheduler (runs at 9:00 AM every day)"""

    script_path = Path(__file__).parent / 'scraper.py'
    python_exe = sys.executable

    task_name = "HurriyetNewsScraper"

    # Create task via XML file
    xml_content = f'''<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2026-04-28T09:00:00</Date>
    <Author>News Scraper</Author>
    <Description>Fetches news from hurriyet.com.tr daily at 09:00</Description>
    <URI>\\{task_name}</URI>
  </RegistrationInfo>
  <Triggers>
    <CalendarTrigger>
      <StartBoundary>2026-04-28T09:00:00</StartBoundary>
      <Enabled>true</Enabled>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>S-1-5-21-3623811015-3361044348-30300820-1001</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>true</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <Duration>PT10M</Duration>
      <WaitTimeout>PT1H</WaitTimeout>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT30M</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>{python_exe}</Command>
      <Arguments>"{script_path}"</Arguments>
      <WorkingDirectory>{Path(__file__).parent}</WorkingDirectory>
    </Exec>
  </Actions>
</Task>'''

    try:
        # Save XML temporarily
        xml_file = 'task.xml'
        with open(xml_file, 'w', encoding='utf-16') as f:
            f.write(xml_content)

        print("Registering task in Windows Task Scheduler...")

        # Remove existing task if present
        delete_cmd = f'schtasks /delete /tn "{task_name}" /f'
        subprocess.run(delete_cmd, shell=True, capture_output=True)

        # Create new task via PowerShell
        powershell_cmd = f'''
        Register-ScheduledTask -Xml (Get-Content -Path "{xml_file}" -Raw) -TaskName "{task_name}" -Force
        '''

        result = subprocess.run(
            ['powershell', '-Command', powershell_cmd],
            capture_output=True,
            text=True
        )

        if result.returncode == 0 or "error" not in result.stderr.lower():
            print(f"✓ Task '{task_name}' registered successfully!")
            print("Schedule: Every day at 09:00")
        else:
            # Fallback: use schtasks directly
            print("Trying alternative method...")
            cmd = f'schtasks /create /tn "{task_name}" /tr "python \\"{script_path}\\"" /sc daily /st 09:00 /f'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

            if result.returncode == 0:
                print(f"✓ Task '{task_name}' registered successfully!")
                print("Schedule: Every day at 09:00")
            else:
                print(f"✗ Error: {result.stderr}")

        # Remove temporary XML file
        if os.path.exists(xml_file):
            os.remove(xml_file)

    except Exception as e:
        print(f"✗ Error: {e}")

def remove_task_scheduler():
    """Removes the task from Windows Task Scheduler"""
    task_name = "HurriyetNewsScraper"

    try:
        cmd = f'schtasks /delete /tn "{task_name}" /f'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"✓ Task '{task_name}' removed.")
        else:
            print(f"✗ Error: {result.stderr}")

    except Exception as e:
        print(f"✗ Error: {e}")

def check_task_status():
    """Checks the task status"""
    task_name = "HurriyetNewsScraper"

    try:
        cmd = f'schtasks /query /tn "{task_name}"'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"✓ Task '{task_name}' is active\n")
            print(result.stdout)
        else:
            print(f"✗ Task not found or error: {result.stderr}")

    except Exception as e:
        print(f"✗ Error: {e}")

def install_requirements():
    """Installs required libraries"""
    requirements = ['requests', 'beautifulsoup4', 'tabulate']

    print("Installing required libraries...")

    for package in requirements:
        try:
            __import__(package.replace('-', '_'))
            print(f"✓ {package} already installed")
        except ImportError:
            print(f"  Installing {package}...")
            subprocess.run([sys.executable, '-m', 'pip', 'install', package],
                          capture_output=True)
            print(f"✓ {package} installed")

if __name__ == '__main__':
    print("="*60)
    print("NEWS SCRAPER SETUP")
    print("="*60)

    # Install required libraries first
    install_requirements()

    print("\n" + "="*60)
    print("1. Set up daily task (at 9:00 AM)")
    print("2. Check task status")
    print("3. Remove task")
    print("4. Exit")
    print("="*60)

    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
        setup_task_scheduler()
    elif choice == '2':
        check_task_status()
    elif choice == '3':
        remove_task_scheduler()
    elif choice == '4':
        print("Exiting...")
    else:
        print("✗ Invalid choice")
