# 查询授权控制对象信息（LST ALLOWEDOBJ）

- [命令功能](#ZH-CN_MMLREF_0209653649__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653649__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653649__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653649__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653649__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653649)

**适用NF：NRF**

该命令用于在NRF上查询访问授权控制策略的NF对象信息。

查询所有授权控制对象信息，请不要输入任何参数信息。

查询某个授权控制对象信息，请输入具体的授权对象名称。

## [注意事项](#ZH-CN_MMLREF_0209653649)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209653649)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653649)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJNAME | 授权对象名称 | 可选必选说明：可选参数<br>参数含义：该参数表示设置访问授权控制策略的NF对象名称，该参数通过LST ALLOWEDOBJNAME命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。该字段值需要全系统唯一，只能由字母（A-Z或者a-z）、数字（0-9）组成，不能以数字开始。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653649)

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

## [输出结果说明](#ZH-CN_MMLREF_0209653649)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 授权对象名称 | 该参数表示设置访问授权控制策略的NF对象名称，该参数通过LST ALLOWEDOBJNAME命令获取。 |
| FQDN | 该参数表示设置访问授权控制策略的NF对象的FQDN。 |
