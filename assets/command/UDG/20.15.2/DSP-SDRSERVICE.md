---
id: UDG@20.15.2@MMLCommand@DSP SDRSERVICE
type: MMLCommand
name: DSP SDRSERVICE（显示SDRC中的Service信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SDRSERVICE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRSERVICE（显示SDRC中的Service信息）

## 功能

该命令用于查询SDRC中指定APP的Service信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPTYPE | App类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示业务类型，可通过<br>[**DSP SDRPOLICYKEYS**](显示SDRC中的策略Key信息（DSP SDRPOLICYKEYS）_22132897.md)<br>: POLICYTYPE=Service;命令获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SDRSERVICE]] · SDRC中的Service信息（SDRSERVICE）

## 使用实例

使用如下命令查询SDRC中缓存的服务实例信息：

```
%%DSP SDRSERVICE: APPTYPE=2001;%%
RETCODE = 0  操作成功

结果如下
--------
实例 ID                POD ID                  容器 ID                       进程号  进程 ID                          

13358201890078505928  vup-pod-010-107-0-165  vup-pod-010-107-0-165__121  0       vup-pod-010-107-0-165__121__0
13358201890079338002  vup-pod-110-107-1-11   vup-pod-110-107-1-11__121   0       vup-pod-110-107-1-11__121__0
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SDRSERVICE.md`
