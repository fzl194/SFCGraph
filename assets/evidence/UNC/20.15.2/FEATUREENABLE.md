# 特性使能（OPR FEATUREENABLE）

- [命令功能](#ZH-CN_MMLREF_0214567234__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0214567234__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0214567234__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0214567234__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0214567234)

该命令用于网元动态上线一系列特性。

## [注意事项](#ZH-CN_MMLREF_0214567234)

无

#### [操作用户权限](#ZH-CN_MMLREF_0214567234)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0214567234)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODINSTANCENUM | Pod实例个数列表 | 可选必选说明：必选参数<br>参数含义：Pod实例个数列表。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| EXTENDEDATTR | 扩展属性 | 可选必选说明：可选参数<br>参数含义：该参数为预留功能，无需填写。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| FUNCTIONSETNAME | 网络功能集名称 | 可选必选说明：可选参数<br>参数含义：网络功能集名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| MEID | 网元ID | 可选必选说明：可选参数<br>参数含义：该参数用于标识Pod所在的网元ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~40。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0214567234)

- OPR FEATUREENABLE: PODINSTANCENUM="usn-pod:1/usnom-pod:1",;
  ```
  functionsetModel=false 场景：
  %%OPR FEATUREENABLE: PODINSTANCENUM="usn-pod:1/usnom-pod:1";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  结果说明  =  NULL
  执行结果  =  请求已接受
  (结果个数 = 1)

  ---    END
  ```
- OPR FEATUREENABLE: PODINSTANCENUM="usn-pod:1/usnom-pod:1",FUNCTIONSETNAME="MME";
  ```
  functionsetModel=true 场景：
  %%OPR FEATUREENABLE: PODINSTANCENUM="usn-pod:1/usnom-pod:1",FUNCTIONSETNAME="MME";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  结果说明  =  NULL
  执行结果  =  请求已接受
  (结果个数 = 1)

  ---    END
  ```
