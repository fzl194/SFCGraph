---
id: UNC@20.15.2@MMLCommand@LST EPSQOSACTION
type: MMLCommand
name: LST EPSQOSACTION（查询EPS QoS控制动作配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EPSQOSACTION
command_category: 查询类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- EPS QoS配置
- EPS QoS控制动作
status: active
---

# LST EPSQOSACTION（查询EPS QoS控制动作配置）

## 功能

**适用NF：PGW-C**

该命令用于查询4G用户QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。

## 注意事项

- 带宽取值为4294967295时，表示无效值。
- 当不输入参数时，系统查询所有配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QoS Profile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EPSQOSACTION]] · EPS QoS控制动作配置（EPSQOSACTION）

## 使用实例

查询“QOSPROFILENAME”为“test”，“QCI”为“2”的上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作：

```
%%LST EPSQOSACTION: QOSPROFILENAME="test";%%
RETCODE = 0  操作成功

操作结果如下
------------
          QoS Profile名  =  test
                  QCI值  =  2
下行保证带宽(千比特/秒)  =  2222
      超过下行GBR的处理  =  降级
上行保证带宽(千比特/秒)  =  4294967295
      超过上行GBR的处理  =  降级
下行最大带宽(千比特/秒)  =  4294967295
      超过下行MBR的处理  =  降级
上行最大带宽(千比特/秒)  =  4294967295
      超过上行MBR的处理  =  降级
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询EPS-QoS控制动作配置（LST-EPSQOSACTION）_09652483.md`
