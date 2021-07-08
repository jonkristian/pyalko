"""
Generated by generator/generator.py - 2021-07-05 19:30:20.823243
"""
import pytest


@pytest.fixture()
def device_fixture_response():
    return {
        "thingName": "bb4636bcc0cfdf78b37f00e28172b614e73acb90",
        "thingType": "ALKO-ROBOLINHO",
        "thingAttributes": {
            "articleNumber": "119999",
            "firmwareMain": "2103A-SW",
            "firmwareMainLocalization": "SW",
            "firmwareWifi": "1.5.4",
            "firmwareWifiDriver": "V19.6.1",
            "fotaMode": "off",
            "hardwareVersionMain": "1D",
            "hardwareVersionWifi": "1D",
            "serialNumberMain": "0000-000000",
            "serialNumberWifi": "00000000000000000",
            "thingModel": "Robolinho800",
            "thingName": "bb4636bcc0cfdf78b37f00e28172b614e73acb90",
            "thingType": "ALKO-ROBOLINHO",
        },
        "accessInformation": {
            "accessAdmin": True,
            "thingName": "bb4636bcc0cfdf78b37f00e28172b614e73acb90",
            "userEmail": "user@example.com",
            "accessId": "00000000-0000-0000-0000-000000000000",
            "accessAlias": "Robolinho800",
            "userId": "0000000000",
            "accessCreated": "2021-06-10T09:55:43.801Z",
        },
        "accesses": [
            {
                "accessAdmin": True,
                "thingName": "bb4636bcc0cfdf78b37f00e28172b614e73acb90",
                "userEmail": "user@example.com",
                "accessId": "0000B42A-79EC-4504-3121-FC5D50E14A94",
                "accessAlias": "Robolinho800",
                "userId": "0000000000",
                "accessCreated": "2021-06-10T09:55:43.801Z",
            }
        ],
        "thingState": {
            "state": {
                "reported": {
                    "isConnected": True,
                    "rssi": -65,
                    "batteryLevel": 25,
                    "operationState": "WORKING",
                    "operationSubState": "READY",
                    "operationSituation": "OPERATION_PERMITTED",
                    "operationError": {
                        "code": 999,
                        "type": "ISSUE",
                        "description": "UNKNOWN",
                    },
                    "nextOperation": 0,
                    "remainingDuration": 203,
                    "operationTimeTotal": 15410,
                    "operationTimeMowing": 2940,
                    "operationTimeWheelMotorLeft": 2819,
                    "operationTimeWheelMotorRight": 2819,
                    "operationTimeBlade": 2361,
                    "mowingCycles": 112,
                    "chargingCycles": 77,
                    "remainingBladeLifetime": 65,
                    "rtc": "2021-06-26T13:37:00",
                    "languageSettings": {
                        "selected": "English",
                        "supported": [
                            "English",
                            "Deutsch",
                            "Italiano",
                            "Français",
                            "Español",
                            "Svenska",
                            "Norsk",
                            "Suomi",
                            "Dansk",
                            "Dutch",
                        ],
                    },
                    "chargingCurrent": 1500,
                    "tiltSlope": 24,
                    "entryPoints": [1614, 1581, 3163, 4745],
                    "rainSensor": True,
                    "rainDelay": 0,
                    "ecoMode": False,
                    "boundaryOverlap": 0,
                    "mowingWindows": {
                        "monday": {
                            "window_1": {
                                "activityMode": True,
                                "marginMode": False,
                                "startHour": 10,
                                "startMinute": 0,
                                "duration": 420,
                                "entryPoint": 33,
                            },
                            "window_2": {
                                "activityMode": True,
                                "marginMode": True,
                                "startHour": 19,
                                "startMinute": 0,
                                "duration": 120,
                                "entryPoint": 33,
                            },
                        },
                        "tuesday": {
                            "window_1": {
                                "activityMode": True,
                                "marginMode": False,
                                "startHour": 10,
                                "startMinute": 0,
                                "duration": 420,
                                "entryPoint": 33,
                            },
                            "window_2": {
                                "activityMode": False,
                                "marginMode": False,
                                "startHour": 19,
                                "startMinute": 0,
                                "duration": 120,
                                "entryPoint": 33,
                            },
                        },
                        "wednesday": {
                            "window_1": {
                                "activityMode": True,
                                "marginMode": False,
                                "startHour": 10,
                                "startMinute": 0,
                                "duration": 420,
                                "entryPoint": 33,
                            },
                            "window_2": {
                                "activityMode": True,
                                "marginMode": True,
                                "startHour": 19,
                                "startMinute": 0,
                                "duration": 120,
                                "entryPoint": 33,
                            },
                        },
                        "thursday": {
                            "window_1": {
                                "activityMode": True,
                                "marginMode": False,
                                "startHour": 10,
                                "startMinute": 0,
                                "duration": 420,
                                "entryPoint": 33,
                            },
                            "window_2": {
                                "activityMode": False,
                                "marginMode": False,
                                "startHour": 19,
                                "startMinute": 0,
                                "duration": 120,
                                "entryPoint": 33,
                            },
                        },
                        "friday": {
                            "window_1": {
                                "activityMode": True,
                                "marginMode": False,
                                "startHour": 7,
                                "startMinute": 0,
                                "duration": 180,
                                "entryPoint": 33,
                            },
                            "window_2": {
                                "activityMode": True,
                                "marginMode": False,
                                "startHour": 17,
                                "startMinute": 0,
                                "duration": 120,
                                "entryPoint": 33,
                            },
                        },
                        "saturday": {
                            "window_1": {
                                "activityMode": True,
                                "marginMode": False,
                                "startHour": 10,
                                "startMinute": 0,
                                "duration": 420,
                                "entryPoint": 33,
                            },
                            "window_2": {
                                "activityMode": False,
                                "marginMode": False,
                                "startHour": 19,
                                "startMinute": 0,
                                "duration": 120,
                                "entryPoint": 32,
                            },
                        },
                        "sunday": {
                            "window_1": {
                                "activityMode": False,
                                "marginMode": False,
                                "startHour": 0,
                                "startMinute": 0,
                                "duration": 0,
                                "entryPoint": 32,
                            },
                            "window_2": {
                                "activityMode": False,
                                "marginMode": False,
                                "startHour": 0,
                                "startMinute": 0,
                                "duration": 0,
                                "entryPoint": 32,
                            },
                        },
                    },
                    "situationFlags": {
                        "operationPermitted": True,
                        "batteryWeak": False,
                        "batteryFailure": False,
                        "batteryWeakSticky": False,
                        "mowingWindow": True,
                        "marginMowingCompleted": False,
                        "userInteraction": False,
                        "loopSignalValid": True,
                        "chargerContact": False,
                        "chargerActive": False,
                        "chargerAllowsRestart": False,
                        "chargerFailure": False,
                        "manualOperation": False,
                        "robotIsActive": True,
                        "issueDisplay": False,
                        "homingTriggerSchedule": False,
                        "homingTriggerBatteryWaek": False,
                        "homingTriggerUserRequest": False,
                        "homingTriggerRain": False,
                        "homingTriggerTemperature": False,
                        "homingTriggerMowingUnitOverload": False,
                        "homingTriggerRestart": False,
                        "dayCancelled": False,
                        "rainDetected": False,
                        "rainAllowsMowing": True,
                        "temperatureMonitoringActive": True,
                        "temperatureAllowsMowing": True,
                        "temperatureAllowsHoming": True,
                        "temperatureAllowsCharging": True,
                        "wheelMotorTemperatureHigh": False,
                        "stopAfterIssue": False,
                        "bladeService": True,
                    },
                }
            },
            "version": 23650,
            "timestamp": 1624707712,
        },
        "pim": {
            "articleNumber": "119999",
            "ean": "4003718356373",
            "name": "",
            "additionalDocuments": [
                {
                    "docname": "Manual_119999_02_0.pdf",
                    "doctype": "BED",
                    "version": "02",
                    "fullpath": "https://alko-garden.de/out/media/additional_documents/119999/Manual_119999_02_0.pdf",
                },
                {
                    "docname": "Conf_119999_03_0.pdf",
                    "doctype": "KONF",
                    "version": "03",
                    "fullpath": "https://alko-garden.de/out/media/additional_documents/119999/Conf_119999_03_0.pdf",
                },
            ],
            "brand": [{"name": "AL-KO"}],
            "images": [
                "https://pim.al-ko.com/products/inTouchApp/119999_Robo_800-W_cut_out.png"
            ],
        },
    }