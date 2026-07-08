---
id: UNC@20.15.2@MMLCommand@LST SCTPPARA
type: MMLCommand
name: LST SCTPPARA（查询SCTP协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCTPPARA
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
- SMSF
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

# LST SCTPPARA（查询SCTP协议参数）

## 功能

**适用网元：SGSN、MME、AMF** 、 **SMSF**

该命令用于查询SCTP协议参数表中指定的记录。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTPPARAINDEX | SCTP协议参数索引 | 可选必选说明：可选参数<br>参数含义：该参数在系统范围内部唯一标识一条SCTP协议参数。<br>取值范围：0~65534<br>默认值：无<br>说明：如果不输入，则表示查询系统内所有SCTP协议参数表中的记录。 |
| SCTPPARANAME | SCTP协议参数名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP协议的参数名的链路信息。<br>取值范围：1~32<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCTPPARA]] · SCTP协议参数（SCTPPARA）

## 使用实例

不输入SCTP协议参数索引，查询已经配置的所有SCTP协议参数表中的记录：

LST SCTPPARA:;

```
%%LST SCTPPARA:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
         SCTP协议参数索引  =  3
           RTO最小值(ms)  =  450
           RTO最大值(ms)  =  6000
           RTO初始值(ms)  =  600
          RTO ALPHA值(%)  =  40
           RTO BETA值(%)  =  90
            心跳间隔(ms)  =  3000
        偶联最大重发次数  =  5
        路径最大重发次数  =  4
            最大入流个数  =  17
            最大出流个数  =  17
            拥塞结束门限  =  40
            拥塞最低门限  =  60
            拥塞最高门限  =  80
发送消息时是否计算校验和  =  是
接收消息时是否计算校验和  =  是
          校验和算法类型  =  CRC32
      绑定定时器时长(ms)  =  10
      延迟定时器时长(ms)  =  200
            IPv4 MTU大小  =  1500
            IPv6 MTU大小  =  1280
          SCTP协议参数名  =  sctppara1
          错包率故障门限  =  5
          错包率恢复门限  =  3
        单偶联最小收包数  =  100
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SCTPPARA.md`
