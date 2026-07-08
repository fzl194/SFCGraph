---
id: UDG@20.15.2@MMLCommand@LST XHEADER
type: MMLCommand
name: LST XHEADER（查询扩展头域）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: XHEADER
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- 扩展头域
status: active
---

# LST XHEADER（查询扩展头域）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询扩展头域相关配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| XHEADERNAME | 扩展头域名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置扩展头域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/XHEADER]] · 扩展头域（XHEADER）

## 使用实例

- 查询名称为testxheader的扩展头域配置：
  ```
  LST XHEADER: XHEADERNAME="testxheader";
  ```
  ```

  RETCODE = 0 操作成功

  扩展头域信息
  -------------------
  扩展头域名称 = testxheader
    扩展头域 = x-mms
    扩展头域 = 1
   配置域名称 = NULL
  (结果个数 = 1)

  --- END
  ```
- 查询所有扩展头域配置：
  ```
  LST XHEADER:;
  ```
  ```

  RETCODE = 0 操作成功

  扩展头域信息
  -------------------
  扩展头域名称 扩展头域 扩展头域取值 配置域名称

  testxheader x-mms 6 NULL
  testxheader1 x-mms 1 NULL
  (结果个数 = 2)

  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询扩展头域（LST-XHEADER）_82753031.md`
