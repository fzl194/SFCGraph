---
id: UDG@20.15.2@MMLCommand@DSP UPDIAMDICTSTAT
type: MMLCommand
name: DSP UPDIAMDICTSTAT（显示Diameter字典加载状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: UPDIAMDICTSTAT
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter管理
- Diameter字典管理
- 加载状态
status: active
---

# DSP UPDIAMDICTSTAT（显示Diameter字典加载状态）

## 功能

**适用NF：UPF**

该命令用于查询Diameter字典的加载状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ITEM | 选项 | 可选必选说明：必选参数<br>参数含义：该参数用于指定状态输出类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LOAD_STAT：字典加载状态。<br>- PATH_STAT：字典加载路径状态。<br>默认值：无<br>配置原则：指定参数类型为LOAD_STAT时，输出参数中进程ID显示为“ALL”表示某个POD上需要加载字典的所有进程。 |

## 操作的配置对象

- [Diameter字典加载状态（UPDIAMDICTSTAT）](configobject/UDG/20.15.2/UPDIAMDICTSTAT.md)

## 使用实例

- 查询当前UPF Diameter字典加载状态：
  ```
  DSP UPDIAMDICTSTAT: ITEM=LOAD_STAT;
  ```
  ```

  RETCODE = 0  操作成功

  结果如下:
  -------------------
  POD名称       进程 ID  数据字典加载状态  结果

  updiam-pod-0  ALL      成功              NULL
  updiam-pod-1  ALL      成功              NULL
  (结果个数 = 2)

  ---    END
  ```
- 查询当前UPF Diameter字典加载路径状态：
  ```
  DSP UPDIAMDICTSTAT: ITEM=PATH_STAT;
  ```
  ```

  RETCODE = 0  操作成功

  Diamter字典加载路径状态
  -----------------------
  结果  =  
  配置字典路径:
  状态 = 加载成功
  应用        字典序号  路径  
  SWM         1         EPC_STANDARD

  加载字典路径:
  状态 = 加载成功
  应用        字典序号  路径  
  SWM         1         EPC_STANDARD

  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示Diameter字典加载状态（DSP-UPDIAMDICTSTAT）_45432686.md`
