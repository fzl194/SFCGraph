---
id: UNC@20.15.2@MMLCommand@DSP COMMSTATMCR
type: MMLCommand
name: DSP COMMSTATMCR（显示通信统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: COMMSTATMCR
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- 扩展调测
- 平台调测
- 通信调测
status: active
---

# DSP COMMSTATMCR（显示通信统计）

## 功能

**适用网元：MME**

该命令用于遇到系统内部通信消息处理有问题时，查询通信统计。

## 注意事项

当只输入必选参数时，由于输出结果内容过多，会导致在结果输出区域的“通用维护”页签中无法显示全部内容，建议在结果输出区单击右键选用“重定向”输出。该命令为调测命令，用于华为技术支持定位问题，如需使用，请联系华为技术支持。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1~63位字符串<br>默认值：无 |
| PROCTYPE | 进程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询通信统计的进程类型。<br>数据来源：无。<br>取值范围：<br>“SAP”<br>，<br>“SRP”<br>，<br>“OMP”<br>默认值： 无。 |
| PROCNO | 进程序列号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询通信统计的进程序号。<br>数据来源：无。<br>取值范围：0~20<br>默认值： 无。 |
| MSGSTATTYPE | 统计类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询通信统计的统计类型。<br>数据来源：无。<br>取值范围：<br>- “MSG_FLOW（消息流类型统计）”<br>- “RECV_PID（接收PID）”<br>- “SOCK_IDX（SOCK索引）”<br>默认值： 无。 |
| MSGFLOW | 消息流类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定查询通信统计的消息流类型。<br>数据来源：无。<br>取值范围：<br>- “SDUP（SDUP消息流）”<br>默认值： 无。 |
| RECVPID | 接收PID | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定查询通信统计的接收PID。<br>数据来源：无。<br>取值范围：0~300<br>默认值： 无。 |
| SOCKIDX | Socket索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定查询通信统计的Socket索引。<br>数据来源：无。<br>取值范围：0~300<br>默认值： 无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/COMMSTATMCR]] · 通信统计（COMMSTATMCR）

## 使用实例

查询MCR_SP_RU_0065下SAP进程SDUP消息流的通信统计：

DSP COMMSTATMCR: RUNAME="MCR_SP_RU_0065", PROCTYPE=SAP, PROCNO=0, MSGSTATTYPE=MSG_FLOW, MSGFLOW=SDUP;

```
%%DSP COMMSTATMCR: RUNAME="MCR_SP_RU_0065", PROCTYPE=SAP, PROCNO=0, MSGSTATTYPE=MSG_FLOW, MSGFLOW=SDUP;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
        RU名称  =  MCR_SP_RU_0065
      进程类型  =  SAP
    进程序列号  =  0
      统计类型  =  Msg flow type
      统计信息  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示通信统计(DSP-COMMSTATMCR)_71851001.md`
