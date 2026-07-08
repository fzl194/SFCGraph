---
id: UNC@20.15.2@MMLCommand@LST EPSQCI2PRER8
type: MMLCommand
name: LST EPSQCI2PRER8（查询EPS QCI到Pre-R8 QoS映射规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EPSQCI2PRER8
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- PreR8 QoS配置
- EPS QCI映射到PreR8
status: active
---

# LST EPSQCI2PRER8（查询EPS QCI到Pre-R8 QoS映射规则）

## 功能

**适用NF：PGW-C、GGSN**

该命令用来显示SAE架构下，Rel-8 QoS参数和Pre Rel-8(R99/R98) QoS参数的映射规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QCI | QCI值 | 可选必选说明：可选参数<br>参数含义：该参数表示Qos流量级别值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EPSQCI2PRER8]] · EPS QCI到Pre-R8 QoS映射规则（EPSQCI2PRER8）

## 使用实例

查询“QCI”为“1”的R8 QoS到Pre-R8 QoS映射规则：

```
%%LST EPSQCI2PRER8: QCI=1;%%
RETCODE = 0  操作成功

结果如下
--------
            QCI值  =  1
         业务类型  =  会话类
   通信处理优先级  =  N/A
     信令传输优化  =  不优化
       源统计描述  =  语音
最大SDU长度(byte)  =  1500
    发送错误的SDU  =  不检测
   传输时延(毫秒)  =  100
        SDU误码率  =  1E-2
   残留比特误码率  =  1E-5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询EPS-QCI到Pre-R8-QoS映射规则（LST-EPSQCI2PRER8）_09652501.md`
