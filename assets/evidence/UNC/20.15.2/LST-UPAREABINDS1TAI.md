# 查询UPF服务区名称绑定的4G TAI范围（LST UPAREABINDS1TAI）

- [命令功能](#ZH-CN_MMLREF_0209652670__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652670__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652670__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652670__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209652670__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209652670)

**适用NF：SGW-C、PGW-C**

该命令用于查询UPF服务区名称绑定的4G TAI范围。

## [注意事项](#ZH-CN_MMLREF_0209652670)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209652670)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652670)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | UPF服务区名称 | 可选必选说明：可选参数<br>参数含义：该参数用于标识UPF服务区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与命令LST UPAREA查询结果中的AREANAME保持一致；且该AREANAME在命令LST UPAREA查询结果中对应的AREATYPE取值应为S1TAI。 |

## [使用实例](#ZH-CN_MMLREF_0209652670)

- 查询UPF服务区名称为"UPAREA1"的区域绑定的4G TAI。 LST UPAREABINDS1TAI: AREANAME="UPAREA1";
  ```
  %%LST UPAREABINDS1TAI: AREANAME="UPAREA1";%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
                     UPF服务区名称  =  uparea1
  UPF服务区名称绑定4G TAI范围起始值  =  123010001
  UPF服务区名称绑定4G TAI范围结束值  =  123011111
  (结果个数 = 1)
  ```
- 查询所有UPF服务区名称绑定的4G TAI。 LST UPAREABINDS1TAI:;
  ```
  %%LST UPAREABINDS1TAI:;%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  UPF服务区名称  UPF服务区名称绑定4G TAI范围起始值  UPF服务区名称绑定4G TAI范围结束值
 
  s1area1001     123030000                         123030009               
  s1area1001     1230310000                        1230310009              
  uparea1        123010001                         123011111               
  (结果个数 = 3)
  ```

## [输出结果说明](#ZH-CN_MMLREF_0209652670)

| 输出项名称 | 输出项解释 |
| --- | --- |
| UPF服务区名称 | 该参数用于标识UPF服务区名称。 |
| UPF服务区名称绑定4G TAI范围起始值 | 该参数用于标识UPF服务区名称绑定4G TAI范围起始值。 |
| UPF服务区名称绑定4G TAI范围结束值 | 该参数用于标识UPF服务区名称绑定4G TAI范围结束值。 |
