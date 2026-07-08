---
id: UNC@20.15.2@MMLCommand@DSP DIAMDICTSTAT
type: MMLCommand
name: DSP DIAMDICTSTAT（显示Diameter字典加载状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DIAMDICTSTAT
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter字典管理
- 加载状态
status: active
---

# DSP DIAMDICTSTAT（显示Diameter字典加载状态）

## 功能

**适用NF：PGW-C、SMF**

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

- [[configobject/UNC/20.15.2/DIAMDICTSTAT]] · Diameter字典加载状态（DIAMDICTSTAT）

## 使用实例

- 查询当前UNC Diameter字典加载状态：
  ```
  DSP DIAMDICTSTAT:ITEM=LOAD_STAT;
  ```
  ```

  RETCODE = 0  操作成功

  Diamter字典加载状态
  -------------------
                       POD名称  =  uncpod-0
                       进程 ID  =  ALL
              数据字典加载状态  =  失败
  第一套字典gy-ccr.xml加载状态  =  成功
  第二套字典gy-ccr.xml加载状态  =  不可用
           cer-cea.xml加载状态  =  成功
  (结果个数 = 1)

  ---    END
  ```
- 查询当前UNC Diameter字典加载路径状态：
  ```
  DSP DIAMDICTSTAT:ITEM=PATH_STAT;
  ```
  ```

  RETCODE = 0  操作成功

  Diamter字典加载路径状态
  -----------------------
  结果  =  
  Configured Dict Path:
  Status = Loaded
  Application   DictNo    Path  
  GY            1       CUSTOM1
  GX            1       CUSTOM1
  S6B           1       EPC_STANDARD
  GY            2       CUSTOM2

  Loaded Dict Path:
  Status = Loaded
  Application   DictNo    Path  
  GY            1       CUSTOM1
  GX            1       CUSTOM1
  S6B           1       EPC_STANDARD
  GY            2       CUSTOM2

  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示Diameter字典加载状态（DSP-DIAMDICTSTAT）_09897252.md`
