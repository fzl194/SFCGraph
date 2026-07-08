---
id: UNC@20.15.2@MMLCommand@LST ALLOWEDOBJ
type: MMLCommand
name: LST ALLOWEDOBJ（查询授权控制对象信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ALLOWEDOBJ
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 授权管理
- 访问授权控制
- 访问授权对象管理
status: active
---

# LST ALLOWEDOBJ（查询授权控制对象信息）

## 功能

**适用NF：NRF**

该命令用于在NRF上查询访问授权控制策略的NF对象信息。

查询所有授权控制对象信息，请不要输入任何参数信息。

查询某个授权控制对象信息，请输入具体的授权对象名称。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJNAME | 授权对象名称 | 可选必选说明：可选参数<br>参数含义：该参数表示设置访问授权控制策略的NF对象名称，该参数通过LST ALLOWEDOBJNAME命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。该字段值需要全系统唯一，只能由字母（A-Z或者a-z）、数字（0-9）组成，不能以数字开始。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ALLOWEDOBJ]] · 授权控制对象信息（ALLOWEDOBJ）

## 使用实例

- 查询所有受控对象的记录：
  ```
  LST ALLOWEDOBJ:;
  %%LST ALLOWEDOBJ:;%%
  RETCODE = 0  执行成功

  结果如下
  -------------------------
  对象名称         FQDN       

  objname001       huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org      
  objname002       huawei1.com.apn.epc.mnc001.mcc123.3gppnetwork.org           
  (结果个数 = 2)
  ```
- 查询对象名称为objname001的受控对象的记录：
  ```
  LST ALLOWEDOBJ: OBJNAME="objname001";
  %%LST ALLOWEDOBJ:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  授权对象名称  =  objname001
          FQDN  =  huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ALLOWEDOBJ.md`
