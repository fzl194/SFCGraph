---
id: UNC@20.15.2@MMLCommand@LST NRFKEY
type: MMLCommand
name: LST NRFKEY（查询NRF密钥）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFKEY
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 授权管理
- 密钥管理
status: active
---

# LST NRFKEY（查询NRF密钥）

## 功能

**适用NF：NRF**

该命令用于查询NRF的密钥信息，其对应的公钥信息，在NF上通过LST SBINRFKEY命令查询配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYNAME | 密钥名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示在NRF上配置的密钥名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFKEY]] · NRF密钥（NRFKEY）

## 使用实例

- 查询所有NRF密钥信息：
  ```
  LST NRFKEY:;
  %%LST NRFKEY:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  密钥名称   密钥HASH值                                                        密钥状态        NRF密钥ID开关            NRF密钥ID 
  nrfkey001  15aaad897b01d8d1353285bda39c50c39d8b9c61296167c1955f737c944d0a3a  未激活状态          打开                 nrfkid1
  nrfkey002  15aaad897b01d8d1353285bda39c50c39d8b9c61296167c1955f737c944d0a3a  未激活状态          关闭                  
  (结果个数 = 2)
  ```
- 查询密钥名称为keyname001的NRF密钥信息：
  ```
  LST NRFKEY: KEYNAME="keyname001";
  %%LST NRFKEY: KEYNAME="keyname001";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  密钥名称  =  keyname001
  密钥HASH值  =  15aaad897b01d8d1353285bda39c50c39d8b9c61296167c1955f737c944d0a3a
  密钥状态  =  未激活状态
  NRF密钥ID开关  =  打开
  NRF密钥ID  =  nrfkid1
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFKEY.md`
