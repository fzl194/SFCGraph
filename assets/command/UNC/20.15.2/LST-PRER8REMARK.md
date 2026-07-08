---
id: UNC@20.15.2@MMLCommand@LST PRER8REMARK
type: MMLCommand
name: LST PRER8REMARK（查询Pre-R8 QoS到TOS/DSCP的映射规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PRER8REMARK
command_category: 查询类
applicable_nf:
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- PreR8 QoS配置
- PreR8 Qos映射ToS_DSCP
status: active
---

# LST PRER8REMARK（查询Pre-R8 QoS到TOS/DSCP的映射规则）

## 功能

**适用NF：GGSN**

该命令用于查询QoS参数映射到IP报文头中的TOS（服务类型）或者DSCP（区别服务编码点）的映射配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QosProfile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PRER8REMARK]] · Pre-R8 QoS到TOS/DSCP的映射规则（PRER8REMARK）

## 使用实例

查询指定QoS Profile名称对应的QoS的DSCP的映射信息：

```
LST PRER8REMARK:QOSPROFILENAME="qosprofile1";%%
RETCODE = 0  操作成功

结果如下
-----------------------
QoS Profile名  =  qosprofile1
     业务级别  =  会话业务
     用户级别  =  普通用户
     标记类型  =  DSCP
         DSCP  =  AF
       AF级别  =  1
 AF丢弃优先级  =  1
        TOS值  =  0
       DSCP值  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PRER8REMARK.md`
