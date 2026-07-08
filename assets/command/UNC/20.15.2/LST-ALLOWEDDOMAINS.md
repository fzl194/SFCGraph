---
id: UNC@20.15.2@MMLCommand@LST ALLOWEDDOMAINS
type: MMLCommand
name: LST ALLOWEDDOMAINS（查询允许访问的域名）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ALLOWEDDOMAINS
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
- NF域名访问授权控制
status: active
---

# LST ALLOWEDDOMAINS（查询允许访问的域名）

## 功能

**适用NF：NRF**

该命令用于查询指定NF类型/NF实例允许访问的FQDN。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJNAME | 授权对象名称 | 可选必选说明：可选参数<br>参数含义：该参数表示设置访问授权控制的NF对象名称，该参数通过LST ALLOWEDOBJNAME命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ALLOWEDDOMAINS]] · 允许访问的域名（ALLOWEDDOMAINS）

## 使用实例

- 查询所有对象允许访问的FQDN：
  ```
  LST ALLOWEDDOMAINS:;
  %%LST ALLOWEDDOMAINS:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  授权对象名称  允许访问该对象的FQDN                               记录状态    

  objname001    huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org  添加未提交  
  objname002    huawei1.com.apn.epc.mnc001.mcc123.3gppnetwork.org  添加未提交  
  objname003    huawei1.com.apn.epc.mnc001.mcc123.3gppnetwork.org  添加未提交  
  (结果个数 = 3)
  ```
- 查询对象为objname001允许访问的FQDN：
  ```
  LST ALLOWEDDOMAINS: OBJNAME="objname001";
  %%LST ALLOWEDDOMAINS: OBJNAME="objname001";%%
  RETCODE = 0  操作成功

  结果如下
  --------
          授权对象名称  =  objname001
  允许访问该对象的FQDN  =  huawei1.com.apn.epc.mnc001.mcc123.3gppnetwork.org
              记录状态  =  添加未提交
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ALLOWEDDOMAINS.md`
