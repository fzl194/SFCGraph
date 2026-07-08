---
id: UNC@20.15.2@MMLCommand@LST TALST
type: MMLCommand
name: LST TALST（查询跟踪区列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TALST
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- TA List管理
status: active
---

# LST TALST（查询跟踪区列表）

## 功能

**适用网元：MME**

该命令用于查看跟踪区列表。通过此命令，可以查询到某个跟踪区列表和在该跟踪区列表中的跟踪区。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TALISTID | TA List 标号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询跟踪区列表标识。<br>取值范围：0~65534<br>默认值：无 |
| TAI | TAI | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询跟踪区列表中的跟踪区。<br>取值范围：9~10位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TALST]] · 跟踪区列表（TALST）

## 使用实例

1. 查看所有跟踪区列表和与其对应的跟踪区：
  LST TALST:;
  ```
  %%LST TALST:;%%
  RETCODE = 0  操作成功。

  结果如下
  --------------
   TA List 标号  TAI         描述

   0             308015101   AREA1
   0             308015102   AREA2
   1             308015103   AREA3
   2             308015110   AREA4
  (结果个数 = 4)
  ---    END
  ```
2. 查看包含跟踪区标识为308015101的跟踪区列表：
  LST TALST: TAI="308015101
  ```
  %%LST TALST: TAI="308015101";%%
  RETCODE = 0  操作成功。

  结果如下
  --------------
  TA List 标号  =  0
           TAI  =  308015101
          描述  =  AREA1
  (结果个数 = 1)
  ---    END 
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-TALST.md`
