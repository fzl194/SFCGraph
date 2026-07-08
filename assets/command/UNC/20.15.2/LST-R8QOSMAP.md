---
id: UNC@20.15.2@MMLCommand@LST R8QOSMAP
type: MMLCommand
name: LST R8QOSMAP（查询EPS QoS参数到Pre-R8 QoS参数映射规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: R8QOSMAP
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- QoS兼容性管理
- EPS QoS参数到Pre-R8 QoS参数映射
status: active
---

# LST R8QOSMAP（查询EPS QoS参数到Pre-R8 QoS参数映射规则）

## 功能

**适用网元：MME**

此命令用于查看EPS QoS参数到Pre-R8 QoS参数映射规则。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QCI | QoS 级别标识 | 可选必选说明：可选参数<br>参数含义：待查询映射规则所对应QoS的级别。QoS共分为9级业务服务质量，由QCI的值来标识。<br>取值范围：1～254<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/R8QOSMAP]] · EPS QoS参数到Pre-R8 QoS参数映射规则（R8QOSMAP）

## 使用实例

查询所有记录：

LST R8QOSMAP:;

```
%%LST R8QOSMAP:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
 QoS 级别标识  流量等级              最大SDU长度  发送次序                保留BER   发送错误SDU  SDU误码率  发送控制优先级    传递时延

 1             Conversational class  150          Without delivery order  保留BER7  不检查       1*10^-2    Priority level 3  10      
 2             Conversational class  150          Without delivery order  保留BER7  不检查       1*10^-3    Priority level 3  15      
 3             Conversational class  150          Without delivery order  保留BER7  不检查       1*10^-3    Priority level 3  10      
 4             Streaming class       150          Without delivery order  保留BER7  不检查       1*10^-4    Priority level 3  18      
 5             Interactive class     150          Without delivery order  保留BER7  不检查       1*10^-4    Priority level 1  10      
 6             Interactive class     150          Without delivery order  保留BER7  不检查       1*10^-4    Priority level 1  18      
 7             Interactive class     150          Without delivery order  保留BER7  不检查       1*10^-3    Priority level 2  10      
 8             Interactive class     150          Without delivery order  保留BER7  不检查       1*10^-4    Priority level 3  18      
 9             Background class      150          Without delivery order  保留BER7  不检查       1*10^-4    Priority level 3  18      
 65            Conversational class  150          Without delivery order  保留BER7  不检查       1*10^-2    Priority level 3  10      
 66            Conversational class  150          Without delivery order  保留BER7  不检查       1*10^-2    Priority level 3  10      
 69            Interactive class     150          Without delivery order  保留BER7  不检查       1*10^-4    Priority level 1  18      
 70            Interactive class     150          Without delivery order  保留BER7  不检查       1*10^-4    Priority level 1  18        
(结果个数 = 13)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-R8QOSMAP.md`
