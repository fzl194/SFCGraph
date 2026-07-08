---
id: UNC@20.15.2@MMLCommand@LST N40QUOTACTRL
type: MMLCommand
name: LST N40QUOTACTRL（查询N40接口配额的控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N40QUOTACTRL
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 全局配置
status: active
---

# LST N40QUOTACTRL（查询N40接口配额的控制参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询N40接口配额的控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@N40QUOTACTRL]] · N40接口配额的控制参数（N40QUOTACTRL）

## 使用实例

查询N40接口配额的控制参数：

```
%%LST N40QUOTACTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
       CHF下发零配额的动作  =  正常处理
   CHF下发零时长配额的动作  =  去活会话
RG级阻塞处理时间间隔(分钟)  =  0
      在线计费上报统计类型  =  缺省
              费率切换模式  =  缺省
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-N40QUOTACTRL.md`
