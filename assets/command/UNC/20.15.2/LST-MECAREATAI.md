---
id: UNC@20.15.2@MMLCommand@LST MECAREATAI
type: MMLCommand
name: LST MECAREATAI（查询5G MEC TAI信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MECAREATAI
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AM策略和UE策略管理
- 本地特色业务区域管理
- 本地特色业务区域TAI成员管理
status: active
---

# LST MECAREATAI（查询5G MEC TAI信息）

## 功能

**适用NF：AMF**

该命令用于查询指定区域或者系统中配置的所有区域的跟踪区成员。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示区域（例如：商场或景区）的标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~1024。<br>默认值：无<br>配置原则：<br>AREAID需要通过ADD MECAREA命令配置添加。 |

## 操作的配置对象

- [5G MEC TAI信息（MECAREATAI）](configobject/UNC/20.15.2/MECAREATAI.md)

## 使用实例

- 查询标识为“1”的区域成员信息，执行如下命令：
  ```
  %%LST MECAREATAI: AREAID=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
        区域标识  =  1
             MCC  =  123
             MNC  =  45
  跟踪区起始编码  =  123456
  跟踪区结束编码  =  123456
        描述信息  =  West Lake
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中当前配置的所有5G MEC区域的跟踪区信息，执行如下命令：
  ```
  %%LST MECAREATAI:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
        区域标识  =  1
             MCC  =  123
             MNC  =  45
  跟踪区起始编码  =  123456
  跟踪区结束编码  =  123456
        描述信息  =  West Lake
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G-MEC-TAI信息（LST-MECAREATAI）_84932185.md`
