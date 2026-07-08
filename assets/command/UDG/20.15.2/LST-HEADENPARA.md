---
id: UDG@20.15.2@MMLCommand@LST HEADENPARA
type: MMLCommand
name: LST HEADENPARA（查询头增强参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HEADENPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 头增强控制
- 头增强参数
status: active
---

# LST HEADENPARA（查询头增强参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询头增强配置的参数信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HEADERENNAME | 头增强名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置头增强名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD HEADEN命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HEADENPARA]] · 头增强参数（HEADENPARA）

## 使用实例

- 假如运营商想查看名称为“headen1”头增强配置的参数记录：
  ```
  LST HEADENPARA: HEADERENNAME="headen1";
  ```
  ```

  RETCODE = 0  操作成功

  头增强参数信息
  --------------
        头增强名称  =  headen1
       TCP分片开关  =  使能（开启）
       TCP分片长度  =  1300
        配置域名称  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 假如运营商想查看所有的头增强配置的参数记录：
  ```
  LST HEADENPARA:;
  ```
  ```

  RETCODE = 0  操作成功

  头增强参数信息
  --------------
  头增强名称  TCP分片开关      TCP分片长度    配置域名称
                             
  headen1     使能（开启）     1300           NULL
  headen2     使能（开启）     1400           NULL
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-HEADENPARA.md`
