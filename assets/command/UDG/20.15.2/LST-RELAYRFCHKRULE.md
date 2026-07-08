---
id: UDG@20.15.2@MMLCommand@LST RELAYRFCHKRULE
type: MMLCommand
name: LST RELAYRFCHKRULE（查询媒体中继引用检查规则）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RELAYRFCHKRULE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继引用检查规则
status: active
---

# LST RELAYRFCHKRULE（查询媒体中继引用检查规则）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询媒体中继引用检查规则。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYRFCHKNAME | 媒体中继引用检查名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定媒体中继引用检查名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RELAYRFCHKRULE]] · 媒体中继引用检查规则（RELAYRFCHKRULE）

## 使用实例

假如需要查询一组媒体中继引用检查规则，则命令如下：

```
LST RELAYRFCHKRULE: RELAYRFCHKNAME="test";
```

```

RETCODE = 0  操作成功
 
结果如下
------------------------
   媒体中继引用检查名称  =  test
               检测模式  =  白名单模式
      黑名单URL列表名称  =  NULL
      白名单URL列表名称  =  test
未携带Referer字段的动作  =  缺省处理动作
           检查失败动作  =  拒绝
             忽略Scheme  =  使能
             配置域名称  =  NULL
(结果个数 = 1)
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RELAYRFCHKRULE.md`
