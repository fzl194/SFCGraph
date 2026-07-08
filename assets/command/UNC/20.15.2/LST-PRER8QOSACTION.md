---
id: UNC@20.15.2@MMLCommand@LST PRER8QOSACTION
type: MMLCommand
name: LST PRER8QOSACTION（查询Pre-R8 QoS控制动作配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PRER8QOSACTION
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
- PreR8 QoS控制动作
status: active
---

# LST PRER8QOSACTION（查询Pre-R8 QoS控制动作配置）

## 功能

**适用NF：GGSN**

该命令用于查询QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QoS Profile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>QOSPROFILENAME字段值必须先在QOSPROFILE或QOSGLOBAL对象中添加成功。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PRER8QOSACTION]] · Pre-R8 QoS控制动作配置（PRER8QOSACTION）

## 使用实例

查询“QOSPROFILENAME”为“test”的上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作：

```
%%LST PRER8QOSACTION:;%%
RETCODE = 0  操作成功

结果如下
--------
     QoS Profile名  =  test
          业务类型  =  会话类
下行GBR(千比特/秒)  =  121
 超过下行GBR的处理  =  降级
上行GBR(千比特/秒)  =  44
 超过上行GBR的处理  =  降级
下行MBR(千比特/秒)  =  144
 超过下行MBR的处理  =  拒绝
上行MBR(千比特/秒)  =  45
 超过上行MBR的处理  =  降级
             THP值  =  0
     超过THP的处理  =  降级
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Pre-R8-QoS控制动作配置（LST-PRER8QOSACTION）_09651831.md`
