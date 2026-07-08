---
id: UNC@20.15.2@MMLCommand@DSP UCFSVRLNKSTAT
type: MMLCommand
name: DSP UCFSVRLNKSTAT（显示UCF链路状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: UCFSVRLNKSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- UCF管理
- UCF服务器链路状态
status: active
---

# DSP UCFSVRLNKSTAT（显示UCF链路状态）

## 功能

该命令用于查询UCF与报表服务器之间的链路状态。

## 注意事项

执行命令前请确认UCF服务处于上线状态。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UCFSVRNAME | UCF服务器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于请求系统显示到指定UCF服务器的链路状态；若不输入，则显示本端到所有对端UCF服务器的链路状态信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |
| PROTOCOLTYPE | 协议类型 | 可选必选说明：可选参数<br>参数含义：该参数用于请求系统显示指定协议类型的链路状态；若不输入，则显示环境中所有协议类型的信息。<br>数据来源：本端规划<br>取值范围：<br>- TCP（TCP）<br>- SFTP（SFTP）<br>- FTP（FTP）<br>- UDP（UDP）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UCF链路状态（UCFSVRLNKSTAT）](configobject/UNC/20.15.2/UCFSVRLNKSTAT.md)

## 使用实例

运营商A查询UCF本端与报表服务器的链路状态信息：

```
%%DSP UCFSVRLNKSTAT:;%%
RETCODE = 0  操作成功

结果如下
--------
UCF POD ID     UCF服务器名称  本端IP类型  本端IPv4地址  本端IPv6地址  本端端口  对端IP类型  对端IPv4地址  对端IPv6地址  对端端口  协议类型  链路状态  

ucfexec-pod-1  UCFSVR         IPv4        10.10.0.6     ::            6666      IPv4        10.10.0.66    ::            10500     TCP       正常      
ucfexec-pod-0  UCFSVR         IPv4        10.10.0.6     ::            6667      IPv4        10.10.0.66    ::            10500     TCP       正常      
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示UCF链路状态（DSP-UCFSVRLNKSTAT）_63673347.md`
