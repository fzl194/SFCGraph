---
id: UDG@20.15.2@MMLCommand@LST CONTCATEGROUP
type: MMLCommand
name: LST CONTCATEGROUP（查询内容分类组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CONTCATEGROUP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容分类组配置
status: active
---

# LST CONTCATEGROUP（查询内容分类组）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询所有配置的内容分类组信息，或者根据内容分类组名称显示相关配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONTCATEGNAME | 内容分类组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置内容分类组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [内容分类组（CONTCATEGROUP）](configobject/UDG/20.15.2/CONTCATEGROUP.md)

## 使用实例

查询所有配置的内容分类组信息：

```
LST CONTCATEGROUP:;
```

```

RETCODE = 0  操作成功

内容分类组信息
--------------
内容分类组名称        内容分类类型  内容分类值  内容分类起始值  内容分类结束值  优先级  内容分类名称  配置域名称  

cf_contcategrprange1  范围          0           1               100             0       NULL          NULL        
cf_contcategrprange1  优先级        0           0               0               65535   NULL          NULL        
cf_contcategrprange2  范围          0           1               200             0       NULL          NULL        
cf_contcategrprange2  优先级        0           0               0               65535   NULL          NULL        
cf_contcategrprange3  范围          0           1               280             0       NULL          NULL        
cf_contcategrprange3  优先级        0           0               0               65535   NULL          NULL        
cf_contcategrprange4  范围          0           300             400             0       NULL          NULL        
cf_contcategrprange4  优先级        0           0               0               65535   NULL          NULL        
cf_contcategrprange5  范围          0           405             500             0       NULL          NULL        
cf_contcategrprange5  优先级        0           0               0               65535   NULL          NULL        
cf_contcategrprange6  优先级        0           0               0               65535   NULL          domain1     
cf_contcategrprange6  名称          10000       0               0               0       news          domain1     
(结果个数 = 12)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询内容分类组（LST-CONTCATEGROUP）_43357961.md`
