# 查询APN IPv6接口ID配置（LST APNIPV6INFID）

- [命令功能](#ZH-CN_MMLREF_0296242072__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296242072__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296242072__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296242072__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0296242072__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0296242072)

**适用NF：PGW-C、GGSN、SMF**

此命令用于查询指定APN下的IMSI作为用户的IPv6地址Interface ID功能开关配置信息。

## [注意事项](#ZH-CN_MMLREF_0296242072)

无

#### [操作用户权限](#ZH-CN_MMLREF_0296242072)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0296242072)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0296242072)

- 查询APN名称为huawei.com的APN的IMSI作为用户的IPv6地址Interface ID功能配置：
  ```
  %%LST APNIPV6INFID: APN="huawei.com";%%
  RETCODE = 0  操作成功

  结果如下
  --------
                            APN  =  huawei.com
  配置IMSI作为IPv6 Interface ID  =  继承全局
  (结果个数 = 1)

  ---    END
  ```
- 查询所有APN的IMSI作为用户的IPv6地址Interface ID功能配置：
  ```
  %%LST APNIPV6INFID:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  APN                   配置IMSI作为IPv6 Interface ID  

  0168apn1.com          继承全局                       
  0168apn2.com          继承全局                       
  a.mnc003.mcc460.gprs  继承全局                                             
  huawei.com            继承全局                       
  (结果个数 = 4)

  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0296242072)

| 输出项名称 | 输出项解释 |
| --- | --- |
| APN名称 | 该参数用于指定APN实例名。 |
| 配置IMSI作为IPv6 Interface ID | 该参数用于控制开启和关闭IMSI作为用户的IPv6地址Interface ID功能。 |
