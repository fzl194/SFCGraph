---
id: UNC@20.15.2@MMLCommand@SET SGWCHGPAUSE
type: MMLCommand
name: SET SGWCHGPAUSE（设置SGW的计费暂停能力）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SGWCHGPAUSE
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 计费暂停管理
- SGW计费暂停管理
status: active
---

# SET SGWCHGPAUSE（设置SGW的计费暂停能力）

## 功能

**适用NF：SGW-C**

该命令用于设置SGW计费暂停能力的相关参数。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 当SGW-U与PGW-U合一部署时，由U面根据本地策略决策是否计费暂停，C面不支持计费暂停功能。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| RELEASE | DDNREJECT | DATATHRESHOLDSW | DATATHRESHOLD | DATAACTION |
| --- | --- | --- | --- | --- |
| DISABLE | DISABLE | DISABLE | 500 | BUFFER |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELEASE | S1 Release触发计费暂停开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示原因值为Abnormal Release of Radio Link的S1 Release流程触发计费暂停功能开关。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SGWCHGPAUSE查询当前参数配置值。<br>配置原则：无 |
| DDNREJECT | DDN寻呼失败触发计费暂停开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示DDN寻呼失败触发计费暂停功能开关。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SGWCHGPAUSE查询当前参数配置值。<br>配置原则：无 |
| DATATHRESHOLDSW | 下行报文阈值触发计费暂停开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示下行报文阈值触发计费暂停功能开关。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SGWCHGPAUSE查询当前参数配置值。<br>配置原则：无 |
| DATATHRESHOLD | 下行报文丢包阈值 | 可选必选说明：该参数在"DATATHRESHOLDSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于控制IDLE状态用户触发计费暂停功能的下行报文个数阈值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535，单位是个。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SGWCHGPAUSE查询当前参数配置值。<br>配置原则：无 |
| DATAACTION | 计费暂停时下行报文处理动作 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开始计费暂停功能后下行报文处理动作。<br>数据来源：全网规划<br>取值范围：<br>- “BUFFER（缓存）”：开启SGW计费暂停功能后缓存下行报文。<br>- “DROP（丢弃）”：开启SGW计费暂停功能后丢弃下行报文。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SGWCHGPAUSE查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGWCHGPAUSE]] · SGW的计费暂停功能（SGWCHGPAUSE）

## 使用实例

设置DDN寻呼失败时触发计费暂停功能，且开始计费暂停后，丢弃下行报文：

```
%%SET SGWCHGPAUSE: DDNREJECT=ENABLE, DATAACTION=DROP;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SGWCHGPAUSE.md`
