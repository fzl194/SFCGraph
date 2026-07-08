---
id: UNC@20.15.2@MMLCommand@LST IUPFSELFAIL
type: MMLCommand
name: LST IUPFSELFAIL（查询I-UPF选择失败处理方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IUPFSELFAIL
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- I-UPF选择失败处理
status: active
---

# LST IUPFSELFAIL（查询I-UPF选择失败处理方式）

## 功能

**适用NF：SMF**

该命令用于查询当SMF/I-SMF在Service Request流程中选择I-UPF失败时的处理方式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IUPFSELFAIL]] · I-UPF选择失败处理方式（IUPFSELFAIL）

## 使用实例

查询所有IUPFSELFAIL记录：

```
%%LST IUPFSELFAIL:;%%
RETCODE = 0  操作成功

结果如下
--------
                     开关  =  不使能
             失败处理方式  =  释放会话
释放会话时携带的NAS原因值  =  #38 网络侧失败
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IUPFSELFAIL.md`
