---
id: UNC@20.15.2@MMLCommand@LST GTPUCTRL
type: MMLCommand
name: LST GTPUCTRL（查询用户面控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPUCTRL
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 数据转发管理
- GTP-U
- GTP-U参数管理
status: active
---

# LST GTPUCTRL（查询用户面控制参数）

## 功能

**适用网元：SGSN、MME**

该命令用于显示用户面控制参数信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GTPUCTRL]] · 用户面控制参数（GTPUCTRL）

## 使用实例

查询用户面控制参数：

LST GTPUCTRL:;

```
%%LST GTPUCTRL:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
                   新SGSN开始下行时间(100ms)  =  36
                     停止接收切换数据时间(s)  =  3
                GTP-U路径断后多久去活PDP (s)  =  0
   流量更新时是否将PDP信息上报到用户跟踪开关  =  关闭
                    2G支持特殊业务类型扩展头  =  不支持
                    3G透传特殊业务类型扩展头  =  透传
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GTPUCTRL.md`
