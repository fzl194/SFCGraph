---
id: UNC@20.15.2@MMLCommand@LST TALSTPAGINGPLCY
type: MMLCommand
name: LST TALSTPAGINGPLCY（查询TA List寻呼策略配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TALSTPAGINGPLCY
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- 基于TA List寻呼策略管理
status: active
---

# LST TALSTPAGINGPLCY（查询TA List寻呼策略配置）

## 功能

**适用网元：MME**

该命令用于查看基于TA List的寻呼策略配置数据。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TALISTID | TA List标号 | 可选必选说明：可选参数<br>参数含义：该参数用于在MME内唯一标识一个跟踪区列表。一个跟踪区列表由若干跟踪区TA组合而成。<br>数据来源：本端规划<br>取值范围：0~65534。<br>默认值：无 |

## 操作的配置对象

- [TA List寻呼策略配置（TALSTPAGINGPLCY）](configobject/UNC/20.15.2/TALSTPAGINGPLCY.md)

## 使用实例

1. 查询所有TA List寻呼策略配置：
  LST TALSTPAGINGPLCY:;
  ```
  %%LST TALSTPAGINGPLCY:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  -------------------------
  TA List标号     是否关闭精准寻呼     是否配置定时器     T3413(s)     N3413(times)     重寻呼间隔递增值(s)
  1               是                   否                 6            2                0 
  2               是                   是                 3            5                10 
  (结果个数 = 2)

  ---    END
  ```
2. 查询一条TA List寻呼策略配置：
  LST TALSTPAGINGPLCY: TALISTID=2;
  ```
  %%LST TALSTPAGINGPLCY: TALISTID=2;%%
  RETCODE = 0  操作成功。

  输出结果如下
  -------------------------
           TA List标号  =  2
      是否关闭精准寻呼  =  是
        是否配置定时器  =  是
              T3413(s)  =  3
          N3413(times)  =  5
   重寻呼间隔递增值(s)  =  10
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询TA-List寻呼策略配置(LST-TALSTPAGINGPLCY)_72225943.md`
