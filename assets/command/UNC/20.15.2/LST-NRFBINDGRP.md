---
id: UNC@20.15.2@MMLCommand@LST NRFBINDGRP
type: MMLCommand
name: LST NRFBINDGRP（查询对端NRF实例组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFBINDGRP
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF拓扑配置
- NRF实例组成员管理
status: active
---

# LST NRFBINDGRP（查询对端NRF实例组成员）

## 功能

**适用NF：NRF**

该命令用于查询对端NRF实例组的成员。

若要查询所有的对端NRF实例组成员信息，请不要输入任何参数。

若要查询指定某参数对应的对端NRF实例组成员信息，请输入对应参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRFINSTNAME | NRF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示对端NRF实例组中NRF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~38。<br>默认值：无<br>配置原则：无 |
| GROUPNAME | 实例组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示对端NRF实例组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |
| ISREGED | 对端NRF是否注册 | 可选必选说明：可选参数<br>参数含义：该参数用于表示对端NRF是否作为南向NRF在当前NRF注册过。<br>NRF通过此参数提高后续南向路由选择的可靠性：<br>- 对于已注册的对端南向NRF，当前NRF会在本地持有的NF profile中判断其状态是否正常，正常则作为后续路由选择，异常则过滤掉不再选择；<br>- 对于未注册的对端南向NRF不做判断。<br>数据来源：本端规划<br>取值范围：<br>- FALSE（未注册的NRF）<br>- TRUE（已注册的南向NRF）<br>默认值：无<br>配置原则：无 |
| NRFINSTID | NRF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示对端NRF组中当前配置的NRF成员的实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFBINDGRP]] · 对端NRF实例组成员（NRFBINDGRP）

## 使用实例

- 查询所有对端NRF实例组成员：
  ```
  LST NRFBINDGRP:;
  %%LST NRFBINDGRP:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NRF实例名称    实例组名称    对端NRF是否注册   NRF实例标识                           优先级   权重

  nrfinstname001 nrfgroup001   已注册的南向NRF   123e4567-e89b-12d3-a456-426655440000  100      100
  nrfinstname002 nrfgroup002   未注册的NRF       NULL                                  100      100
  (结果个数 = 2)
  ```
- 查询对端NRF实例组中组名称为nrfgroup001的成员：
  ```
  LST NRFBINDGRP: GROUPNAME="nrfgroup001";
  %%LST NRFBINDGRP: GROUPNAME="nrfgroup001";%%
  RETCODE = 0  操作成功

  结果如下
  --------
       NRF实例名称  =  nrfinstname001
        实例组名称  =  nrfgroup001
  对端NRF是否注册   =  已注册的南向NRF
       NRF实例标识  =  123e4567-e89b-12d3-a456-426655440000
            优先级  =  100  
              权重  =  100
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFBINDGRP.md`
