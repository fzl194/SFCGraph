# 显示vProbe收发的单据报文信息（DSP VPROBEPKTSTAT）

- [命令功能](#ZH-CN_MMLREF_0000001439202441__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001439202441__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001439202441__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001439202441__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001439202441__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001439202441)

该命令用于显示vProbe收发的单据报文信息。

## [注意事项](#ZH-CN_MMLREF_0000001439202441)

执行命令前请确认vProbe服务处于上线状态，可通过DSP FUNCTIONSETINFO命令查询确认。

#### [操作用户权限](#ZH-CN_MMLREF_0000001439202441)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001439202441)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODID | vProbe Pod ID | 可选必选说明：可选参数<br>参数含义：该参数用于请求系统显示指定Pod的报文信息；若不输入，则显示环境中所有vprobeexec-pod的报文信息。该参数可以通过DSP POD:TYPE=byType, PODTYPE="vprobeexec-pod", MEID="网元ID";命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| PROTOCOLTYPE | 协议类型 | 可选必选说明：可选参数<br>参数含义：该参数用于请求系统显示指定协议类型的报文信息；若不输入，则显示环境中所有协议类型的信息。该参数可以通过<br>[**LST VPROBESVRIP**](../vProbe服务器IP/查询vProbe报表服务器的接入点IP地址（LST VPROBESVRIP）_89042704.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：<br>- TCP（TCP）<br>- SFTP（SFTP）<br>- UDP（UDP）<br>默认值：无<br>配置原则：无 |
| ACCESSNAME | 接入点名称 | 可选必选说明：可选参数<br>参数含义：该参数用于请求系统显示指定接入点的报文信息；若不输入，则显示环境中所有接入点的信息。该参数可以通过<br>[**LST VPROBESVRIP**](../vProbe服务器IP/查询vProbe报表服务器的接入点IP地址（LST VPROBESVRIP）_89042704.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001439202441)

运营商A查询所有vProbe服务向接入点发送单据报文的信息：

```
%%DSP VPROBEPKTSTAT:;%%
RETCODE = 0  操作成功

结果如下
--------
vProbe Pod ID     协议类型  接入点名称  接收报文数  被流控处理报文数  发送成功报文数  发送失败报文数  发送成功文件数  发送失败文件数  被老化处理文件数  非主向主实例发送文件数  

vprobeexec-pod-0  TCP       ACCESS1     5120        0                 5120            0               0               0               0                 0                       
vprobeexec-pod-1  TCP       ACCESS1     5120        0                 5120            0               0               0               0                 0                       
(结果个数 = 2)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001439202441)

| 输出项名称 | 输出项解释 |
| --- | --- |
| vProbe Pod ID | 该参数用于请求系统显示指定Pod的报文信息；若不输入，则显示环境中所有vprobeexec-pod的报文信息。该参数可以通过DSP POD:TYPE=byType, PODTYPE="vprobeexec-pod", MEID="网元ID";命令查询得到。 |
| 协议类型 | 该参数用于请求系统显示指定协议类型的报文信息；若不输入，则显示环境中所有协议类型的信息。该参数可以通过<br>[**LST VPROBESVRIP**](../vProbe服务器IP/查询vProbe报表服务器的接入点IP地址（LST VPROBESVRIP）_89042704.md)<br>命令查询得到。<br>取值说明：<br>- TCP（TCP）<br>- SFTP（SFTP）<br>- UDP（UDP） |
| 接入点名称 | 该参数用于请求系统显示指定接入点的报文信息；若不输入，则显示环境中所有接入点的信息。该参数可以通过<br>[**LST VPROBESVRIP**](../vProbe服务器IP/查询vProbe报表服务器的接入点IP地址（LST VPROBESVRIP）_89042704.md)<br>命令查询得到。 |
| 接收报文数 | 该参数用于返回当前VPROBEEXEC实例接收到的报文总数，不区分接入点（单位：个）。 |
| 被流控处理报文数 | 该参数用于返回当前VPROBEEXEC服务实例被流控处理的报文总数，不区分接入点（单位：个）。 |
| 发送成功报文数 | 该参数用于返回当前VPROBEEXEC实例向接入点发送成功的报文数（单位：个）。 |
| 发送失败报文数 | 该参数用于返回当前VPROBEEXEC实例向接入点发送失败的报文数（单位：个）。 |
| 发送成功文件数 | 该参数用于返回使用SFTP协议时当前VPROBEEXEC服务实例向接入点发送成功的文件个数（单位：个）。 |
| 发送失败文件数 | 该参数用于返回使用SFTP协议时当前VPROBEEXEC服务实例向接入点发送失败的文件个数（单位：个）。 |
| 被老化处理文件数 | 该参数用于返回使用SFTP协议时当前VPROBEEXEC服务实例老化处理的文件个数，不区分接入点（单位：个）。 |
| 非主向主实例发送文件数 | 该参数为保留字段。 |
