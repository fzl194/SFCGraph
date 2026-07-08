# 查询NRF密钥（LST NRFKEY）

- [命令功能](#ZH-CN_MMLREF_0209652451__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652451__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652451__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652451__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209652451__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209652451)

**适用NF：NRF**

该命令用于查询NRF的密钥信息，其对应的公钥信息，在NF上通过LST SBINRFKEY命令查询配置。

## [注意事项](#ZH-CN_MMLREF_0209652451)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209652451)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652451)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYNAME | 密钥名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示在NRF上配置的密钥名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652451)

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

## [输出结果说明](#ZH-CN_MMLREF_0209652451)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 密钥名称 | 该参数用于表示在NRF上配置的密钥名称。 |
| 密钥HASH值 | 该参数用于表示在NRF上配置的密钥密文的SHA256值。 |
| 密钥状态 | 该参数用于表示NRF上密钥的激活状态。 |
| NRF密钥ID开关 | 该参数用于控制Token申请响应报文中生成的accessToken是否包含NRFKEYID。 |
| NRF密钥ID | 该参数表示NRF上配置的密钥ID，用于标识同一NRF分配的不同Token。 |
