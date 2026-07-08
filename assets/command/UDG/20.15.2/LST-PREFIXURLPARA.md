---
id: UDG@20.15.2@MMLCommand@LST PREFIXURLPARA
type: MMLCommand
name: LST PREFIXURLPARA（查询前缀URL参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PREFIXURLPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- 前缀URL参数
status: active
---

# LST PREFIXURLPARA（查询前缀URL参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询用户模板的前缀URL配置参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USERPROFILE命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PREFIXURLPARA]] · 前缀URL参数（PREFIXURLPARA）

## 使用实例

查询用户模板的前缀URL配置参数：

```
%%LST PREFIXURLPARA:;
```

```
%%
RETCODE = 0  操作成功

前缀URL参数
-----------
       用户模板名称  =  testprofile1
匹配Server IP的开关  =  使能（开启）
     检查Scheme开关  =  使能（开启）
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PREFIXURLPARA.md`
