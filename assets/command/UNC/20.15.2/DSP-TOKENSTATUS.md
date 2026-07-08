---
id: UNC@20.15.2@MMLCommand@DSP TOKENSTATUS
type: MMLCommand
name: DSP TOKENSTATUS（显示Token状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TOKENSTATUS
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- SMF
- GGSN
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- 状态查询
status: active
---

# DSP TOKENSTATUS（显示Token状态）

## 功能

**适用NF：SGW-C、PGW-C、AMF、SMF、GGSN、SMSF、NCG**

该命令用于根据实例id查询token状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | 实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示服务实例的编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>该参数来源于通过DSP INSTANCESTATUS查询到的“INSTANCEID”参数。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TOKENSTATUS]] · Token状态（TOKENSTATUS）

## 使用实例

怀疑token迁移存在问题时查询。获取指定服务实例下的token状态信息。

```
%%DSP TOKENSTATUS:INSTANCEID="12532461132836508461";%%
RETCODE = 0  操作成功
结果如下
------------------------   
服务实例ID           TOKEN ID           TOKEN状态                                      TOKEN状态持续时间           是否稳态

12532461132836508461  53      smooth_dst        20        TRUE
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-TOKENSTATUS.md`
