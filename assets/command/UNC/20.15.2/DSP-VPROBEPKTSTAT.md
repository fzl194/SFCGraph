---
id: UNC@20.15.2@MMLCommand@DSP VPROBEPKTSTAT
type: MMLCommand
name: DSP VPROBEPKTSTAT（显示vProbe收发的单据报文信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: VPROBEPKTSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- vProbe管理
- vProbe单据报文信息
status: active
---

# DSP VPROBEPKTSTAT（显示vProbe收发的单据报文信息）

## 功能

该命令用于显示vProbe收发的单据报文信息。

## 注意事项

执行命令前请确认vProbe服务处于上线状态，可通过DSP FUNCTIONSETINFO命令查询确认。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODID | vProbe Pod ID | 可选必选说明：可选参数<br>参数含义：该参数用于请求系统显示指定Pod的报文信息；若不输入，则显示环境中所有vprobeexec-pod的报文信息。该参数可以通过DSP POD:TYPE=byType, PODTYPE="vprobeexec-pod", MEID="网元ID";命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| PROTOCOLTYPE | 协议类型 | 可选必选说明：可选参数<br>参数含义：该参数用于请求系统显示指定协议类型的报文信息；若不输入，则显示环境中所有协议类型的信息。该参数可以通过<br>[**LST VPROBESVRIP**](../vProbe服务器IP/查询vProbe报表服务器的接入点IP地址（LST VPROBESVRIP）_89042704.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：<br>- TCP（TCP）<br>- SFTP（SFTP）<br>- UDP（UDP）<br>默认值：无<br>配置原则：无 |
| ACCESSNAME | 接入点名称 | 可选必选说明：可选参数<br>参数含义：该参数用于请求系统显示指定接入点的报文信息；若不输入，则显示环境中所有接入点的信息。该参数可以通过<br>[**LST VPROBESVRIP**](../vProbe服务器IP/查询vProbe报表服务器的接入点IP地址（LST VPROBESVRIP）_89042704.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [vProbe收发的单据报文信息（VPROBEPKTSTAT）](configobject/UNC/20.15.2/VPROBEPKTSTAT.md)

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示vProbe收发的单据报文信息（DSP-VPROBEPKTSTAT）_39202441.md`
