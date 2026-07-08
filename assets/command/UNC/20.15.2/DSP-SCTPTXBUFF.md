---
id: UNC@20.15.2@MMLCommand@DSP SCTPTXBUFF
type: MMLCommand
name: DSP SCTPTXBUFF（查询SCTP发送缓冲区）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SCTPTXBUFF
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# DSP SCTPTXBUFF（查询SCTP发送缓冲区）

## 功能

**适用NF：SGSN、MME、AMF**

此命令用于查询SCTP发送缓冲区信息。

## 注意事项

此命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRT | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询方式。<br>取值范围：<br>- PROC（按进程查询）<br>- INTYPE（按接口类型查询）<br>默认值：“PROC（按进程查询）” |
| RUNAME | RU名称 | 可选必选说明：条件可选/必选参数<br>参数含义：该参数用于指定待查询的RU名称。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1~63位字符串<br>默认值 ：无<br>配置原则：“查询方式”参数设置为“PROC（按进程查询）”时，该参数为可选参数；“查询方式”参数设置为“INTYPE（按接口类型查询）”时，该参数为必选参数。 |
| PN | 进程号 | 可选必选说明：条件可选/必选参数<br>参数含义：该参数用于指定查询的SGP的进程号。<br>取值范围： 0~11<br>默认值 ：无<br>配置原则：“查询方式”参数设置为“PROC（按进程查询）”时，该参数为可选参数；“查询方式”参数设置为“INTYPE（按接口类型查询）”时，该参数为必选参数。 |
| IFTYPE | 接口类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定查询的接口类型。<br>前提条件：“查询方式”参数设置为“INTYPE（按接口类型查询）”时，该参数必选。<br>取值范围：<br>- S1（S1）<br>- N2（N2）<br>默认值 ：S1<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCTPTXBUFF]] · SCTP发送缓冲区（SCTPTXBUFF）

## 使用实例

查询N2接口SCTP发送缓冲区，可以用如下命令：

DSP SCTPTXBUFF: SRT=INTYPE, RUNAME="LINK_SP_RU_0064", PN=0, IFTYPE=N2;

```
%%DSP SCTPTXBUFF: SRT=INTYPE, RUNAME="LINK_SP_RU_0064", PN=0, IFTYPE=N2;%%
RETCODE = 0  操作成功

操作结果如下
------------
偶联ID  对端IP地址1   对端端口号  私有发送缓冲区总大小  私有发送缓冲区占用大小  扩展发送缓冲区总大小  扩展发送缓冲区占用大小  发送缓冲区占用率  

198     192.168.0.10  16514       20000                 116                     0                     0                       1%                
200     192.168.1.11  16926       20000                 116                     0                     0                       1%                
(结果个数 = 2)

---    END 
```

查询所有SGP进程上的SCTP发送缓冲区，可以用如下命令：

DSP SCTPTXBUFF: SRT=PROC;

```
%%DSP SCTPTXBUFF: SRT=PROC;%%
RETCODE = 0  操作成功

操作结果如下
------------
RU名称           进程号  S1共享发送缓冲区占用块  N2共享发送缓冲区占用块  迷你端共享区总块  迷你端共享区占用率  

LINK_SP_RU_0064  0       0                       0                       30000000          0%                  
LINK_SP_RU_0065  1       0                       0                       30000000          0%                  
LINK_SP_RU_0064  1       0                       0                       30000000          0%                  
LINK_SP_RU_0065  0       0                       0                       30000000          0%                  
(结果个数 = 4)

---    END 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SCTPTXBUFF.md`
