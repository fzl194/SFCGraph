---
id: UNC@20.15.2@MMLCommand@LST NSMAPPARA
type: MMLCommand
name: LST NSMAPPARA（查询网络切片映射相关参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSMAPPARA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 网络切片映射管理
- 网络切片映射控制参数
status: active
---

# LST NSMAPPARA（查询网络切片映射相关参数）

## 功能

**适用NF：AMF**

该命令用于查询网络切片映射相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSMAPPARA]] · 网络切片映射相关参数（NSMAPPARA）

## 使用实例

查询切片映射相关参数，执行如下命令：

```
%%LST NSMAPPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
           本地切片映射开关  =  打开
漫游用户CFG切片增强功能开关  =  打开
           标准切片映射开关  =  打开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NSMAPPARA.md`
