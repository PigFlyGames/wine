@ stdcall WTSCloseServer(long)
@ stdcall WTSConnectSessionA(long long ptr long)
@ stdcall WTSConnectSessionW(long long ptr long)
@ stdcall WTSDisconnectSession(long long long)
@ stdcall WTSEnumerateProcessesA(long long long ptr ptr)
@ stdcall WTSEnumerateProcessesW(long long long ptr ptr)
@ stdcall WTSEnumerateServersA(ptr long long ptr ptr)
@ stdcall WTSEnumerateServersW(ptr long long ptr ptr)
@ stdcall WTSEnumerateSessionsA(long long long ptr ptr)
@ stdcall WTSEnumerateSessionsW(long long long ptr ptr)
@ stdcall WTSFreeMemory(ptr)
@ stdcall WTSLogoffSession(long long long)
@ stdcall WTSOpenServerA(ptr)
@ stdcall WTSOpenServerW(ptr)
@ stdcall WTSQuerySessionInformationA(long long long ptr ptr)
@ stdcall WTSQuerySessionInformationW(long long long ptr ptr)
@ stdcall WTSQueryUserConfigA(ptr ptr long ptr ptr)
@ stdcall WTSQueryUserConfigW(ptr ptr long ptr ptr)
@ stdcall WTSQueryUserToken(long ptr)
@ stdcall WTSRegisterSessionNotification(long long)
@ stdcall WTSRegisterSessionNotificationEx(long long long)
@ stdcall WTSSendMessageA(long long ptr long ptr long long long ptr long)
@ stdcall WTSSendMessageW(long long ptr long ptr long long long ptr long)
@ stub WTSSetSessionInformationA
@ stub WTSSetSessionInformationW
@ stdcall WTSSetUserConfigA(ptr ptr long ptr long)
@ stdcall WTSSetUserConfigW(ptr ptr long ptr long)
@ stdcall WTSShutdownSystem(long long)
@ stdcall WTSStartRemoteControlSessionA(ptr long long long)
@ stdcall WTSStartRemoteControlSessionW(ptr long long long)
@ stdcall WTSStopRemoteControlSession(long)
@ stdcall WTSTerminateProcess(long long long)
@ stdcall WTSUnRegisterSessionNotification(long)
@ stdcall WTSUnRegisterSessionNotificationEx(long long)
@ stdcall WTSVirtualChannelClose(long)
@ stdcall WTSVirtualChannelOpen(long long ptr)
@ stdcall WTSVirtualChannelOpenEx(long ptr long)
@ stdcall WTSVirtualChannelPurgeInput(long)
@ stdcall WTSVirtualChannelPurgeOutput(long)
@ stdcall WTSVirtualChannelQuery(long long ptr ptr)
@ stdcall WTSVirtualChannelRead(long long ptr long ptr)
@ stdcall WTSVirtualChannelWrite(long ptr long ptr)
@ stdcall WTSWaitSystemEvent(long long ptr)
