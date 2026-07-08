---
id: UNC@20.15.2@MMLCommand@LST APNUPSELPLY
type: MMLCommand
name: LST APNUPSELPLY（查询APN粒度的UP选择策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNUPSELPLY
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- APN粒度的UPF选择策略
status: active
---

# LST APNUPSELPLY（查询APN粒度的UP选择策略）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询APN粒度下的UP选择策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [APN粒度的UP选择策略（APNUPSELPLY）](configobject/UNC/20.15.2/APNUPSELPLY.md)

## 使用实例

查询APN为test下的UP选择策略。

```
%%LST APNUPSELPLY: APN="test";%%
RETCODE = 0  操作成功

结果如下
--------
                            APN  =  test
 基于ULIForSGW位置选择SGW-U开关  =  关
基于位置条件优选主锚点UPF的开关  =  关
      分流场景下共享UPF优选开关  =  关
          基于优先级优选UPF开关  =  关
           合一与优先级优选策略  =  合一优先
        选择合一UPF的优先级策略  =  按TAI/TAIRANGE/SMFSERVINGAREA优先级优选
    位置区S11口与优先级优选策略  =  优先级优先
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN粒度的UP选择策略（LST-APNUPSELPLY）_96242085.md`
