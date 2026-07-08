---
id: UNC@20.15.2@MMLCommand@OPR FEATUREDISABLE
type: MMLCommand
name: OPR FEATUREDISABLE（特性下线）
nf: UNC
version: 20.15.2
verb: OPR
object_keyword: FEATUREDISABLE
command_category: 动作类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 编排管理
- 服务部署管理
status: active
---

# OPR FEATUREDISABLE（特性下线）

## 功能

![](特性下线（OPR FEATUREDISABLE）_14567233.assets/notice_3.0-zh-cn_2.png)

若选择普通下线，内部流程异常时下线任务会失败；修复问题后可以重新下发下线任务。

若选择强制下线，内部流程异常时也会强制将Pod删除。强制下线是高危命令，仅允许在部分特定场景使用（如资源不够情况下的上线失败）。建议操作该动作时，寻求研发工程师支持（如分析是否造成其他数据残留等情况）。

该命令用于网元动态下线一系列特性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | Pod类型列表 | 可选必选说明：必选参数<br>参数含义：Pod类型列表。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| DISABLETYPE | 下线方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务下线方式：<br>若选择普通下线，内部流程异常时下线任务会终止，修复问题后可以重新下发下线任务；<br>若选择强制下线，内部流程异常时也会强制将服务下线。强制下线是高危命令，建议操作该动作时，寻求研发工程师支持。<br>数据来源：本端规划<br>取值范围：<br>- Normal（普通下线）<br>- Force（强制下线）<br>默认值：Normal<br>配置原则：无 |
| FUNCTIONSETNAME | 网络功能集名称 | 可选必选说明：可选参数<br>参数含义：网络功能集名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| MEID | 网元ID | 可选必选说明：可选参数<br>参数含义：该参数用于标识Pod所在的网元ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~40。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [特性下线（FEATUREDISABLE）](configobject/UNC/20.15.2/FEATUREDISABLE.md)

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/特性下线（OPR-FEATUREDISABLE）_14567233.md`
