---
id: UNC@20.15.2@MMLCommand@LST MMEID
type: MMLCommand
name: LST MMEID（查询MMEID配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MMEID
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- MME POOL区管理
- MMEID管理
status: active
---

# LST MMEID（查询MMEID配置）

## 功能

**适用网元：MME**

此命令用于查看MMEID配置表。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MMEID]] · MMEID配置（MMEID）

## 使用实例

查看MMEID配置表：

LST MMEID:;

```
%%LST MMEID:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
       移动国家码  =  308
         移动网码  =  01
      MME组识别码  =  8001
 MME编码（起始值） =  01
      MME编码数目  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MMEID.md`
