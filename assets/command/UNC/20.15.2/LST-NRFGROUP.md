---
id: UNC@20.15.2@MMLCommand@LST NRFGROUP
type: MMLCommand
name: LST NRFGROUP（查询对端NRF实例组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFGROUP
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
- NRF实例组管理
status: active
---

# LST NRFGROUP（查询对端NRF实例组）

## 功能

**适用NF：NRF**

该命令用于查询对端NRF实例组信息。

若要查询全部NRF实例组的配置信息，请不要输入任何参数。

若要查询某NRF实例组的配置信息，请输入“实例组名称”参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | 实例组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示对端NRF实例组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFGROUP]] · 对端NRF实例组（NRFGROUP）

## 使用实例

- 查询所有对端NRF实例组：
  ```
  LST NRFGROUP:;
  %%LST NRFGROUP:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  实例组名称   实例组属性   转发模式     实例组描述  

  nrfgroup001  南向NRF组    递归转发     NULL  
  nrfgroup002  北向NRF组    递归转发     NULL   
  nrfgroup003  东西向NRF组  递归转发     NULL   
  (结果个数 = 3)
  ```
- 查询对端NRF实例组中组名称为nrfgroup001的记录：
  ```
  LST NRFGROUP: GROUPNAME="nrfgroup001";
  %%LST NRFGROUP: GROUPNAME="nrfgroup001";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  实例组名称  =  nrfgroup001
  实例组属性  =  南向NRF组
    转发模式  =  递归转发
  实例组描述  =  NULL
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFGROUP.md`
