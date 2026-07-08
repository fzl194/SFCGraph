---
id: UDG@20.15.2@MMLCommand@DSP CPU
type: MMLCommand
name: DSP CPU（显示资源CPU使用信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CPU
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 系统管理
- 资源管理
- VM管理
status: active
---

# DSP CPU（显示资源CPU使用信息）

## 功能

该命令用于显示资源的CPU使用率信息。

当设备运行缓慢、性能下降时，可使用本命令查看系统资源的CPU使用率是否过高，也可在进行某项操作之前确认当前CPU是否还有足够的处理能力。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESOURCENAME | 资源名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询CPU使用率的资源名称。通过<br>[**DSP RES**](../资源实例管理/显示资源信息（DSP RES）_59036939.md)<br>命令可以查询资源信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：当不输入时显示所有资源的信息。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CPU]] · 资源CPU使用信息（CPU）

## 使用实例

- 显示所有资源的CPU使用率：
  ```
  DSP CPU:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
  资源名称        系统CPU使用率（%） 
  OMU1            13                 
  OMU2            6                  
  (结果个数 = 2)
  ---    END
  ```
- 显示名为OMU1的资源CPU使用率：
  ```
  DSP CPU:RESOURCENAME="OMU1";
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
             资源名称  =  OMU1 
   系统CPU使用率（%）  =  13                 
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-CPU.md`
