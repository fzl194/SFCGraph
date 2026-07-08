---
id: UDG@20.15.2@MMLCommand@LST SRVCERTSCENE
type: MMLCommand
name: LST SRVCERTSCENE（查询配置证书场景）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SRVCERTSCENE
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继证书场景
status: active
---

# LST SRVCERTSCENE（查询配置证书场景）

## 功能

**适用NF：UPF、PGW-U**

该命令用于查询配置证书场景。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCENE | 证书使用场景名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定证书使用场景的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~127。区分大小写，不允许仅大小写不同的重复记录。不支持中文字符，只能由“_”、数字和大小写字母组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRVCERTSCENE]] · 配置证书场景（SRVCERTSCENE）

## 使用实例

查询配置证书场景：

```
LST SRVCERTSCENE:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
    证书使用场景名称  =  test01
           场景类型  =  CA证书场景类型
 证书使用场景中文描述  =  NULL
 证书使用场景英文描述  =  douyin_ca
         配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SRVCERTSCENE.md`
