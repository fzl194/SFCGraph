---
id: UNC@20.15.2@MMLCommand@LST SCALINGCTRL
type: MMLCommand
name: LST SCALINGCTRL（查询扩缩容业务控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCALINGCTRL
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 业务调测
- 扩缩容业务控制参数
status: active
---

# LST SCALINGCTRL（查询扩缩容业务控制参数）

## 功能

**适用网元：MME**

该命令用于查询扩缩容业务控制参数配置。

## 注意事项

无。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组。

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCALINGCTRL]] · 扩缩容业务控制参数（SCALINGCTRL）

## 使用实例

查询扩缩容业务控制参数：

LST SCALINGCTRL:;

```
%%LST SCALINGCTRL:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
          暂态业务保护时长（秒） =  5
           SCTP链路自动均衡开关  =  开启
            GTP路径自动均衡开关  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SCALINGCTRL.md`
