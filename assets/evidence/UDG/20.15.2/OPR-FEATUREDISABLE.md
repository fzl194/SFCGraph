# 特性下线（OPR FEATUREDISABLE）

- [命令功能](#ZH-CN_MMLREF_0214567233__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0214567233__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0214567233__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0214567233__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0214567233)

![](特性下线（OPR FEATUREDISABLE）_14567233.assets/notice_3.0-zh-cn.png)

若选择普通下线，内部流程异常时下线任务会失败；修复问题后可以重新下发下线任务。

若选择强制下线，内部流程异常时也会强制将Pod删除。强制下线是高危命令，仅允许在部分特定场景使用（如资源不够情况下的上线失败）。建议操作该动作时，寻求研发工程师支持（如分析是否造成其他数据残留等情况）。

该命令用于网元动态下线一系列特性。

> **说明**
> 无

#### [操作用户权限](#ZH-CN_MMLREF_0214567233)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0214567233)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | Pod类型列表 | 可选必选说明：必选参数<br>参数含义：Pod类型列表。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| DISABLETYPE | 下线方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务下线方式：<br>若选择普通下线，内部流程异常时下线任务会终止，修复问题后可以重新下发下线任务；<br>若选择强制下线，内部流程异常时也会强制将服务下线。强制下线是高危命令，建议操作该动作时，寻求研发工程师支持。<br>数据来源：本端规划<br>取值范围：<br>- Normal（普通下线）<br>- Force（强制下线）<br>默认值：Normal<br>配置原则：无 |
| FUNCTIONSETNAME | 网络功能集名称 | 可选必选说明：可选参数<br>参数含义：网络功能集名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| MEID | 网元ID | 可选必选说明：可选参数<br>参数含义：该参数用于标识Pod所在的网元ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~40。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0214567233)

- OPR FEATUREDISABLE: PODTYPE="usn-pod/usnom-pod"；
  ```
  functionsetModel=false 场景：
  %%OPR FEATUREDISABLE: PODTYPE="usn-pod/usnom-pod",DISABLETYPE=Normal;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  操作接受结果  =  请求已接受
      结果说明  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- OPR FEATUREDISABLE: PODTYPE="usn-pod/usnom-pod",DISABLETYPE=Normal, FUNCTIONSETNAME="MME";
  ```
  functionsetModel=true 场景：
  %%OPR FEATUREDISABLE: PODTYPE="All Pod",DISABLETYPE=Normal,FUNCTIONSETNAME="MME";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  操作接受结果  =  请求已接受
      结果说明  =  NULL
  (结果个数 = 1)

  ---    END
  ```
