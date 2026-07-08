---
id: UNC@20.15.2@MMLCommand@SET QBCGLBPARA
type: MMLCommand
name: SET QBCGLBPARA（设置QBC计费全局参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: QBCGLBPARA
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 全局配置
status: active
---

# SET QBCGLBPARA（设置QBC计费全局参数）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于设置QBC计费全局参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| QFSTARTRPT | QFTRIGGERFILL | QFTIMECALC |
| --- | --- | --- |
| NOREPORT | DISABLE | PACKETTRIGGERED |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QFSTARTRPT | 激活阶段QoSFlow上报模式 | 可选必选说明：可选参数<br>参数含义：控制用户激活阶段是否上报QoSFlow信息给CHF。<br>数据来源：本端规划<br>取值范围：<br>- “NOREPORT（不上报）”：用户激活时不上报QoSFlow信息。<br>- “REPORT（上报）”：用户激活时上报QoSFlow信息。<br>- “ONLYRPTDFTQF（仅缺省QoSFlow上报）”：用户激活时仅上报缺省QoSFlow信息。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST QBCGLBPARA查询当前参数配置值。<br>配置原则：无 |
| QFTRIGGERFILL | QoSFlow级Trigger填写方式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当仅对PDU会话有效的Trigger发生时，生成的QFI容器是否携带同PDU会话一样的Trigger。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：当仅对PDU会话有效的Trigger发生时，生成的QosFlow容器中不携带同PDU会话一样的Trigger<br>- “ENABLE（使能）”：当仅对PDU会话有效的Trigger发生时，生成的QosFlow容器中携带同PDU会话一样的Trigger<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST QBCGLBPARA查询当前参数配置值。<br>配置原则：<br>缺省时，SMF按Trigger的实际生效粒度携带在PDU会话级或QoSFlow级。<br>当CHF期望在仅对PDU会话有效的Trigger发生且无QoSFlow级Trigger发生时，生成的QFI容器中也携带同PDU会话一样的Trigger，可以使能该功能。 |
| QFTIMECALC | QoSFlow时长计算方式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置CP指示UP QoSFlow的时长计费方式。<br>数据来源：本端规划<br>取值范围：<br>- “PACKETTRIGGERED（PACKETTRIGGERED）”：统计周期内收到第一个数据包到最后一个数据包的时长<br>- “CONTINUOUS（CONTINUOUS）”：从收到URR开始计算连续时长<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST QBCGLBPARA查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QBCGLBPARA]] · QBC计费全局参数（QBCGLBPARA）

## 使用实例

配置激活阶段QoSFlow上报模式为上报：

```
SET QBCGLBPARA: QFSTARTRPT=REPORT;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-QBCGLBPARA.md`
