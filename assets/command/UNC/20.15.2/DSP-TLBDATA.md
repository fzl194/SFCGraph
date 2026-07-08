---
id: UNC@20.15.2@MMLCommand@DSP TLBDATA
type: MMLCommand
name: DSP TLBDATA（显示TLB统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TLBDATA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP服务端负载管理
- 整系统负载管理
- 全局属性
status: active
---

# DSP TLBDATA（显示TLB统计信息）

## 功能

查询TLB控制器上五元组信息、对端IP在各个TCP/Worker进程的分布情况。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DATATYPE | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的TLB数据类型。<br>数据来源：本端规划<br>取值范围：<br>- LOADINFO（负载信息）<br>- STATINTLBC（TLB控制器的统计）<br>- STATINTCP（TCP进程的统计）<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP地址类型 | 可选必选说明：该参数在"DATATYPE"配置为"LOADINFO"时为条件可选参数。<br>参数含义：该参数用于指定对端IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPv4（IPv4地址）”：IPv4地址<br>- “IPv6（IPv6地址）”：IPv6地址<br>默认值：无<br>配置原则：无 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6 | PEERIPV6 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TLBDATA]] · TLB统计信息（TLBDATA）

## 使用实例

- 查询负载信息，可以执行下面的命令。
  ```
  %%DSP TLBDATA: DATATYPE=LOADINFO;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                   HOST ID  =  UNKNOW HOST
                    POD ID  =  vusn-pod-0
         TCP进程Root Token  =  0
          Worker进程全局ID  =  0
       Worker进程静态Token  =  0
                五元组数量  =  0
  与平均链路数的差距百分比  =  0

  (结果个数 = 1)
  ```
- 查询TLB控制器的统计，可以执行下面的命令。
  ```
  %%DSP TLBDATA: DATATYPE=STATINTLBC;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  接收外部TCP SYN报文数量  =  0
  接收直通TCP SYN报文数量  =  0
      接收TCP SYN报文速率  =  0
  接收TCP SYN流控丢包数量  =  0
         五元组策略总数量  =  0
             对端IP总数量  =  0
  (结果个数 = 1)
  ```
- 查询TCP进程的统计，可以执行下面的命令。
  ```
  %%DSP TLBDATA: DATATYPE=STATINTCP;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                                HOST ID  =  UNKNOW HOST
                                 POD ID  =  vusn-pod-0
                      TCP进程Root Token  =  0
  TCP进程接收来自TLB控制器的SYN报文数量  =  0
             TCP进程接收直通SYN包的数量  =  0
             TCP进程上报直通SYN包的数量  =  0
             TCP进程上报直通SYN包的速率  =  0
             TCP进程丢弃直通SYN包的数量  =  0
                  TCP进程上五元组总数量  =  0
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-TLBDATA.md`
