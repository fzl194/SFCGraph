---
id: UNC@20.15.2@MMLCommand@LST SELECTRULEINFO
type: MMLCommand
name: LST SELECTRULEINFO（查询UPF选择规则信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SELECTRULEINFO
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF选择规则信息
status: active
---

# LST SELECTRULEINFO（查询UPF选择规则信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询UPF选择规则信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCF下发的规则名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD UPFBINDSELRULE命令中的“规则名称”参数取值保持一致时，该规则的参数功能生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SELECTRULEINFO]] · UPF选择规则信息（SELECTRULEINFO）

## 使用实例

- 查询"rulename1"的规则信息：
  ```
  %%LST SELECTRULEINFO: RULENAME="rulename1";%%
  RETCODE = 0  操作成功

  结果如下
  --------
             规则名称 = rulename1
             规则功能 = 重点业务保障&用户体验
               优先级 = 0
        是否下发给UPF = 不使能
             下发范围 = 仅对中心UPF(主锚点UPF)生效
  (结果个数 = 1)

  ---    END
  ```
- 查询所有UPF选择规则信息：
  ```
  %%LST SELECTRULEINFO:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  规则名称     规则功能                 优先级            是否下发给UPF            下发范围

  rulename1    重点业务保障&用户体验    0                 不使能                   仅对中心UPF(主锚点UPF)生效
  rulename2    重点业务保障&用户体验    0                 不使能                   仅对中心UPF(主锚点UPF)生效
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UPF选择规则信息（LST-SELECTRULEINFO）_10513594.md`
