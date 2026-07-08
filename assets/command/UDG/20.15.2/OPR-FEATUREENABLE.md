---
id: UDG@20.15.2@MMLCommand@OPR FEATUREENABLE
type: MMLCommand
name: OPR FEATUREENABLE（特性使能）
nf: UDG
version: 20.15.2
verb: OPR
object_keyword: FEATUREENABLE
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 服务部署管理
status: active
---

# OPR FEATUREENABLE（特性使能）

## 功能

该命令用于网元动态上线一系列特性。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODINSTANCENUM | Pod实例个数列表 | 可选必选说明：必选参数<br>参数含义：Pod实例个数列表。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| EXTENDEDATTR | 扩展属性 | 可选必选说明：可选参数<br>参数含义：该参数为预留功能，无需填写。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| FUNCTIONSETNAME | 网络功能集名称 | 可选必选说明：可选参数<br>参数含义：网络功能集名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| MEID | 网元ID | 可选必选说明：可选参数<br>参数含义：该参数用于标识Pod所在的网元ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~40。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [特性使能（FEATUREENABLE）](configobject/UDG/20.15.2/FEATUREENABLE.md)

## 使用实例

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

## 证据

- 原始手册：`evidence/UDG/20.15.2/特性使能（OPR-FEATUREENABLE）_14567234.md`
