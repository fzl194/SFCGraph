---
id: UNC@20.15.2@MMLCommand@DSP PAEUDSSTATUS
type: MMLCommand
name: DSP PAEUDSSTATUS（显示UDS链路状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEUDSSTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 性能模式
status: active
---

# DSP PAEUDSSTATUS（显示UDS链路状态）

## 功能

该命令用于显示UDS链路状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLID | Cell ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定CELLID，可以通过使用命令<br>[**DSP PAENODE**](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PAEUDSSTATUS]] · UDS链路状态（PAEUDSSTATUS）

## 使用实例

显示UDS链路状态：

```
+++    UNC/*MEID:0 MENAME:unc*/        2024-05-20 19:08:53
O&M    #86
%%DSP PAEUDSSTATUS: CELLID="sfpod-0__103__0";%%
RETCODE = 0  操作成功

结果如下
--------
    Cell ID  =  sfpod-0__103__0
UDS链路状态  =
UDS INFORMATION
ENDPOINT TYPE: Server
UDS FILE:/dev/shm/pae_perf_mode_s0.sock
ENDPOINT ID:2
PEER[0]
    ENDPOINT ID:3
    CONNECT FD:459
    CONNECT TIME:2024-05-20 11:28:30
    SEND COUNTER:6
    RECV COUNTER:6
PEER[1]
    ENDPOINT ID:4
    CONNECT FD:464
    CONNECT TIME:2024-05-20 11:28:30
    SEND COUNTER:7
    RECV COUNTER:7

UDS INFORMATION
ENDPOINT TYPE: Client
UDS FILE:/dev/shm/pae_perf_mode_s0.sock
ENDPOINT ID:3
PEER[0]
    ENDPOINT ID:0
    CONNECT FD:458
    CONNECT TIME:2024-05-20 11:28:30
    SEND COUNTER:6
    RECV COUNTER:6

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PAEUDSSTATUS.md`
