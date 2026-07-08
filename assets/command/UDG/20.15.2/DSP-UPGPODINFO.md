---
id: UDG@20.15.2@MMLCommand@DSP UPGPODINFO
type: MMLCommand
name: DSP UPGPODINFO（显示已部署的Pod的版本号）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: UPGPODINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- POD管理
status: active
---

# DSP UPGPODINFO（显示已部署的Pod的版本号）

## 功能

在升级阶段中，可以用来查询pod版本号信息。

> **说明**
> 该命令只能在灰度升级阶段使用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | Pod类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示Pod类型，如sfm-pod，具体类型定义请参考tosca模板中的定义。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~200。<br>默认值：无<br>配置原则：无 |
| VNFVERSION | 归属的网元版本 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VNF版本。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~200。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPGPODINFO]] · 已部署的Pod的版本号（UPGPODINFO）

## 使用实例

DSP UPGPODINFO:;

```
%%DSP UPGPODINFO:;%%
RETCODE = 0  操作成功

结果如下
------------------------
Pod类型      Pod标识                 Pod版本号        归属的网元版本
vusn-pod     vusn-pod-at133es4ed     22.1.RC1.B070    22.1.RC1.B070
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-UPGPODINFO.md`
